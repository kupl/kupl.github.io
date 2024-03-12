# Adapted from https://www.fuzzingbook.org

from types import FrameType, TracebackType
from typing import * 
import matplotlib.pyplot as plt
import time 
import sys
import inspect
import random 
import pickle, hashlib            
from html.parser import HTMLParser

Location = Tuple[str, int]

class Coverage:
    """Track coverage within a `with` block. Use as
    ```
    with Coverage() as cov:
        function_to_be_traced()
    c = cov.coverage()
    ```
    """

    def __init__(self) -> None:
        """Constructor"""
        self._trace: List[Location] = []

    # Trace function
    def traceit(self, frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
        """Tracing function. To be overloaded in subclasses."""
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)

        if event == "line":
            function_name = frame.f_code.co_name
            lineno = frame.f_lineno
            if function_name != '__exit__':  # avoid tracing ourselves:
                self._trace.append((function_name, lineno))

        return self.traceit

    def __enter__(self) -> Any:
        """Start of `with` block. Turn on tracing."""
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    def __exit__(self, exc_type: Type, exc_value: BaseException, 
                 tb: TracebackType) -> Optional[bool]:
        """End of `with` block. Turn off tracing."""
        sys.settrace(self.original_trace_function)
        return None  # default: pass all exceptions

    def trace(self) -> List[Location]:
        """The list of executed lines, as (function_name, line_number) pairs"""
        return self._trace

    def coverage(self) -> Set[Location]:
        """The set of executed lines, as (function_name, line_number) pairs"""
        return set(self.trace())

    def function_names(self) -> Set[str]:
        """The set of function names seen"""
        return set(function_name for (function_name, line_number) in self.coverage())

    def __repr__(self) -> str:
        """Return a string representation of this object.
           Show covered (and uncovered) program code"""
        t = ""
        for function_name in self.function_names():
            # Similar code as in the example above
            try:
                fun = eval(function_name)
            except Exception as exc:
                t += f"Skipping {function_name}: {exc}"
                continue

            source_lines, start_line_number = inspect.getsourcelines(fun)
            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                if (function_name, lineno) in self.trace():
                    t += "# "
                else:
                    t += "  "
                t += "%2d  " % lineno
                t += source_lines[lineno - start_line_number]

        return t

def clock() -> float:
    """
    Return the number of fractional seconds elapsed since some point of reference.
    """
    return time.perf_counter()

class Timer:
    def __init__(self) -> None:
        """Constructor"""
        self.start_time = clock()
        self.end_time = None

    def __enter__(self) -> Any:
        """Begin of `with` block"""
        self.start_time = clock()
        self.end_time = None
        return self

    def __exit__(self, exc_type: Type, exc_value: BaseException,
                 tb: TracebackType) -> None:
        """End of `with` block"""
        self.end_time = clock()  # type: ignore

    def elapsed_time(self) -> float:
        """Return elapsed time in seconds"""
        if self.end_time is None:
            # still running
            return clock() - self.start_time
        else:
            return self.end_time - self.start_time  # type: ignore

def population_coverage(population: List[str], function: Callable) \
        -> Tuple[Set[Location], List[int]]:
    cumulative_coverage: List[int] = []
    all_coverage: Set[Location] = set()

    for s in population:
        with Coverage() as cov:
            try:
                function(s)
            except:
                pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    return all_coverage, cumulative_coverage
  
def html_parser(inp: str) -> None:
  parser = HTMLParser()
  parser.feed(inp)  

def crashme(s: str) -> None:
    if len(s) > 0 and s[0] == 'b':
        if len(s) > 1 and s[1] == 'a':
            if len(s) > 2 and s[2] == 'd':
                if len(s) > 3 and s[3] == '!':
                    raise Exception()
                                                        
def delete_random_character(s: str) -> str:
    """Returns s with a random character deleted"""
    if s == "": return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]

def insert_random_character(s: str) -> str:
    """Returns s with a random character inserted"""
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]
  
def flip_random_character(s: str) -> str:
    """Returns s with a random bit flipped in a random position"""
    if s == "": return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    return s[:pos] + new_c + s[pos + 1:]

def mutate(s: str) -> str:
    """Return s with a random mutation applied"""
    mutators = [
        delete_random_character,
        insert_random_character,
        flip_random_character
    ]
    mutator = random.choice(mutators)
    return mutator(s)  
        
class Seed:
  def __init__(self, data: str) -> None:
    self.data = data 
    self.coverage : Set[Location] = set()
    self.distance : Union[int, float] = -1
    self.energy = 0.0 
    
  def __str__(self) -> str:
    return self.data 
  
  __repr__ = __str__
  
class PowerSchedule:
  def __init__(self) -> None:
    self.path_frequency : Dict = {}
    
  def assignEnergy(self, population: Sequence[Seed]) -> None:
    for seed in population:
      seed.energy = 1 
      
  def normalizedEnergy(self, population: Sequence[Seed]) -> List[float]:
    energy = list(map(lambda seed: seed.energy, population))
    sum_energy = sum(energy)
    assert sum_energy != 0
    norm_energy = list(map(lambda nrg: nrg / sum_energy, energy))
    return norm_energy 
  
  def choose(self, population: Sequence[Seed]) -> Seed:
    self.assignEnergy(population)
    norm_energy = self.normalizedEnergy(population)
    seed: Seed = random.choices(population, weights=norm_energy)[0]
    return seed        

def create_candidate(population, schedule):  
    seed = schedule.choose(population)
    candidate = seed.data 
    
    trials = min(len(candidate), 1 << random.randint(1, 5))
    for i in range(trials):
        candidate = mutate(candidate)
    return candidate

class AFLFastSchedule(PowerSchedule):
    """Exponential power schedule as implemented in AFL"""

    def __init__(self, exponent: float) -> None:
        self.exponent = exponent

    def assignEnergy(self, population: Sequence[Seed]) -> None:
        """Assign exponential energy inversely proportional to path frequency"""
        for seed in population:
            seed.energy = 1 / (self.path_frequency[getPathID(seed.coverage)] ** self.exponent)

def run(function: Callable, inp: str):
    with Coverage() as cov:
        try:
            result = function(inp)
            return True, result, cov.coverage()
        except Exception: 
            return False, None, cov.coverage()

def random_fuzzer(function: Callable, trials: int, max_length : int = 100,  
                  char_start : int = 32, char_range : int = 32):
    data = []
    for i in range(trials):
        length = random.randrange(0, max_length + 1)
        inp = ""
        for i in range(length):
            inp += chr(random.randrange(char_start, char_start + char_range))
        outcome, result, coverage = run(function, inp)
        data.append((inp, outcome, result, coverage))
    return data    
  
def blackbox_fuzzer(function: Callable, seeds : List[str], schedule, trials : int):
    data = []
    population = list(map(lambda x: Seed(x), seeds))
    seed_index = 0
  
    for i in range(trials):
        if seed_index < len(seeds):
            inp = seeds[seed_index]
            seed_index += 1
        else:    
            inp = create_candidate(population, schedule)
            
        outcome, result, coverage = run(function, inp)
        data.append((inp, outcome, result, coverage))

    return data

def greybox_fuzzer(function: Callable, seeds : List[str], schedule, trials : int):
    coverages_seen : Set[frozenset] = set()
    population = [] 
    data = []
    seed_index = 0
    
    for i in range(trials):
        if seed_index < len(seeds):
            inp = seeds[seed_index]
            seed_index += 1
        else:    
            inp = create_candidate(population, schedule)
                
        outcome, result, coverage = run(function, inp)
        data.append((inp, outcome, result, coverage))

        new_coverage = frozenset(coverage)
        if new_coverage not in coverages_seen:
            seed = Seed(inp)
            seed.coverage = new_coverage 
            coverages_seen.add(new_coverage)
            population.append(seed)

    return data

def getPathID(coverage: Any) -> str:
    """Returns a unique hash for the covered statements"""
    pickled = pickle.dumps(sorted(coverage))
    return hashlib.md5(pickled).hexdigest()

def boosted_greybox_fuzzer(function: Callable, seeds : List[str], schedule, trials : int):
    coverages_seen : Set[frozenset] = set()
    population = [] 
    data = []
    seed_index = 0
    schedule.path_frequency = {}
    
    for i in range(trials):
        if seed_index < len(seeds):
            inp = seeds[seed_index]
            seed_index += 1
        else:    
            inp = create_candidate(population, schedule)
                
        outcome, result, coverage = run(function, inp)
        data.append((inp, outcome, result, coverage))

        new_coverage = frozenset(coverage)
        if new_coverage not in coverages_seen:
            seed = Seed(inp)
            seed.coverage = new_coverage 
            coverages_seen.add(new_coverage)
            population.append(seed)
        
        path_id = getPathID(coverage)
        if path_id not in schedule.path_frequency:
            schedule.path_frequency[path_id] = 1
        else:
            schedule.path_frequency[path_id] += 1

    return data

function = crashme
trials = 5000
runs = 100

# function = html_parser
# trials = 5000
# runs = 10

random_data = []
blackbox_data = []
greybox_data = []
boosted_greybox_data = []

for i in range(runs):
    print(f"{i}th run")

    with Timer() as t:
        random_data.append(random_fuzzer(function, trials, max_length = 30)) 
    print(f"random fuzzing took {round(t.elapsed_time(), 1)} seconds")

    with Timer() as t:
        blackbox_data.append(blackbox_fuzzer(function, [" "], PowerSchedule(), trials))
    print(f"blackbox fuzzing took {round(t.elapsed_time(), 1)} seconds")

    with Timer() as t:
        greybox_data.append(greybox_fuzzer(function, [" "], PowerSchedule(), trials))
    print(f"greybox fuzzing took {round(t.elapsed_time(), 1)} seconds")

    with Timer() as t:
        boosted_greybox_data.append(boosted_greybox_fuzzer(function, [" "], AFLFastSchedule(5), trials))
    print(f"boosted greybox fuzzing took {round(t.elapsed_time(), 2)} seconds")

    print()

items = [
   ("random", random_data), 
   ("blackbox", blackbox_data), 
   ("greybox", greybox_data), 
   ("boosted greybox", boosted_greybox_data), 
]

def draw_average_coverage(function, items):
    lines = []
    for (name, data) in items:
        print("draw_average_coverage:", name)
        runs = len(data)
        trials = len(data[0])
        average_coverage = [0] * trials
        for i in range(runs):
            inputs = list(map(lambda x: x[0], data[i]))
            _, cumulative_coverage = population_coverage(inputs, function)
            for j in range(len(cumulative_coverage)):
                average_coverage[j] += cumulative_coverage[j]
        average_coverage = list(map(lambda x: x / runs, average_coverage))
        line, = plt.plot(average_coverage, label=name)      
        lines.append(line)
    plt.legend(handles=lines)
    plt.title("Coverage over time")
    plt.xlabel("# of inputs")
    plt.ylabel("lines covered")
    plt.show()        

draw_average_coverage(function, items)