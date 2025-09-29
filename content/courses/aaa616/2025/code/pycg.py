import sys 
import ast 
import astor
from collections import defaultdict
import graphviz

####################################################

class Var:
    def __init__(self, name): self.name = name
    def __eq__(self, other): return isinstance(other, Var) and self.name == other.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f"Var({self.name})"

class Field:
    def __init__(self, name): self.name = name
    def __eq__(self, other): return isinstance(other, Field) and self.name == other.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f"Field({self.name})"

class Sig:
    def __init__(self, name): self.name = name
    def __eq__(self, other): return isinstance(other, Sig) and self.name == other.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f"Sig({self.name})"

class MethId:
    def __init__(self, name): self.name = name
    def __eq__(self, other): return isinstance(other, MethId) and self.name == other.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f"MethId({self.name})"

class ClassType:
    def __init__(self, name): self.name = name
    def __eq__(self, other): return isinstance(other, ClassType) and self.name == other.name
    def __hash__(self): return hash(self.name)
    def __repr__(self): return f"ClassType({self.name})"

class Label:
    def __init__(self, attrs): self.attrs = attrs
    def __eq__(self, other): return isinstance(other, Label) and self.attrs == other.attrs
    def __hash__(self): return hash(str(self.attrs))
    def __repr__(self): return f"Label({self.attrs})"

class CallSite(Label):
    def __repr__(self): return f"CallSite({self.attrs['lineno']},{self.attrs['col_offset']})"

class AllocSite(Label):
    def __repr__(self): return f"AllocSite({self.attrs['lineno']},{self.attrs['col_offset']})"

class Heap(Label):
    def __repr__(self): return f"Heap({self.attrs['lineno']},{self.attrs['col_offset']})"

class Alloc:
    def __init__(self, var, heap, meth): self.var, self.heap, self.meth = var, heap, meth
    def __eq__(self, o): return (self.var, self.heap, self.meth) == (o.var, o.heap, o.meth)
    def __hash__(self): return hash((self.var, self.heap, self.meth))
    def __repr__(self): return f"Alloc({self.var}, {self.heap}, {self.meth})"

class Move:
    def __init__(self, to_var, from_var): self.to_var, self.from_var = to_var, from_var
    def __eq__(self, o): return (self.to_var, self.from_var) == (o.to_var, o.from_var)
    def __hash__(self): return hash((self.to_var, self.from_var))
    def __repr__(self): return f"Move({self.to_var}, {self.from_var})"

class Load:
    def __init__(self, to_var, base_var, field): self.to_var, self.base_var, self.field = to_var, base_var, field
    def __eq__(self, o): return (self.to_var, self.base_var, self.field) == (o.to_var, o.base_var, o.field)
    def __hash__(self): return hash((self.to_var, self.base_var, self.field))
    def __repr__(self): return f"Load({self.to_var}, {self.base_var}, {self.field})"

class Store:
    def __init__(self, base_var, field, from_var): self.base_var, self.field, self.from_var = base_var, field, from_var
    def __eq__(self, o): return (self.base_var, self.field, self.from_var) == (o.base_var, o.field, o.from_var)
    def __hash__(self): return hash((self.base_var, self.field, self.from_var))
    def __repr__(self): return f"Store({self.base_var}, {self.field}, {self.from_var})"

class VCall:
    def __init__(self, base_var, signature, callsite, in_meth):
        self.base_var, self.signature, self.callsite, self.mid = base_var, signature, callsite, in_meth
    def __eq__(self, o): return (self.base_var, self.signature, self.callsite, self.mid) == (o.base_var, o.signature, o.callsite, o.mid)
    def __hash__(self): return hash((self.base_var, self.signature, self.callsite, self.mid))
    def __repr__(self): return f"VCall({self.base_var}, {self.signature}, {self.callsite}, {self.mid})"

class NormalCall:
    def __init__(self, func_name, callsite, mid): self.func_name, self.callsite, self.mid = func_name, callsite, mid
    def __repr__(self): return f"Call({self.func_name}, {self.callsite}, {self.mid})"

class FormalArg:
    def __init__(self, method_id, index, var): self.method_id, self.index, self.var = method_id, index, var
    def __eq__(self, o): return (self.method_id, self.index, self.var) == (o.method_id, o.index, o.var)
    def __hash__(self): return hash((self.method_id, self.index, self.var))
    def __repr__(self): return f"FormalArg({self.method_id}, {self.index}, {self.var})"

class ThisVar:
    def __init__(self, method_id, var): self.method_id, self.var = method_id, var
    def __eq__(self, o): return (self.method_id, self.var) == (o.method_id, o.var)
    def __hash__(self): return hash((self.method_id, self.var))
    def __repr__(self): return f"ThisVar({self.method_id}, {self.var})"

class HeapType:
    def __init__(self, heap, class_type): self.heap, self.class_type = heap, class_type
    def __eq__(self, o): return (self.heap, self.class_type) == (o.heap, o.class_type)
    def __hash__(self): return hash((self.heap, self.class_type))
    def __repr__(self): return f"HeapType({self.heap}, {self.class_type})"

class ActualArg:
    def __init__(self, callsite, index, var): self.callsite, self.index, self.var = callsite, index, var
    def __eq__(self, o): return (self.callsite, self.index, self.var) == (o.callsite, o.index, o.var)
    def __hash__(self): return hash((self.callsite, self.index, self.var))
    def __repr__(self): return f"ActualArg({self.callsite}, {self.index}, {self.var})"

class FormalReturn:
    def __init__(self, method_id, var): self.method_id, self.var = method_id, var
    def __eq__(self, o): return (self.method_id, self.var) == (o.method_id, o.var)
    def __hash__(self): return hash((self.method_id, self.var))
    def __repr__(self): return f"FormalReturn({self.method_id}, {self.var})"

class ActualReturn:
    def __init__(self, callsite, var): self.callsite, self.var = callsite, var
    def __eq__(self, o): return (self.callsite, self.var) == (o.callsite, o.var)
    def __hash__(self): return hash((self.callsite, self.var))
    def __repr__(self): return f"ActualReturn({self.callsite}, {self.var})"

class Lookup:
    def __init__(self, class_type, sig_, method_id): self.class_type, self.sig, self.method_id = class_type, sig_, method_id
    def __eq__(self, o): return (self.class_type, self.sig, self.method_id) == (o.class_type, o.sig, o.method_id)
    def __hash__(self): return hash((self.class_type, self.sig, self.method_id))
    def __repr__(self): return f"Lookup({self.class_type}, {self.sig}, {self.method_id})"


def collect_class_names(tree):
    return {node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)}

def get_attrs(node):
    return {"lineno": getattr(node, "lineno", None), "col_offset": getattr(node, "col_offset", None)}

def assign_unique_method_ids(tree):
    MethId_map = {}
    method_counter = 1
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            MethId_map[(None, node.name)] = MethId(f"m{method_counter}"); method_counter += 1
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    MethId_map[(node.name, item.name)] = MethId(f"m{method_counter}"); method_counter += 1
    return MethId_map

global_method_sig = Sig("_g_")
global_class_type = ClassType("_G_")
global_method_id = MethId("_gid_")

class Collector(ast.NodeVisitor):
    def __init__(self, tree):
        self.tree = tree 
        self.allocs = set(); self.moves = set(); self.loads = set(); self.stores = set()
        self.vcalls = set(); self.normalcalls = set(); self.formalargs = set()
        self.thisvars = set(); self.heaptypes = set(); self.actualargs = set()
        self.formalreturns = set(); self.actualreturns = set(); self.lookups = set()
        self.class_names = collect_class_names(tree)
        self.current_func = global_method_sig; self.enclosing_class = global_class_type
        lookup_table = assign_unique_method_ids(tree) 
        for (class_type, sig), method_id in lookup_table.items():
            self.lookups.add(Lookup(ClassType(class_type) if class_type else global_class_type, Sig(sig), method_id))
        self.lookups.add(Lookup(global_class_type, global_method_sig, global_method_id))

    def merge(self, other):
        self.allocs |= other.allocs; self.moves |= other.moves; self.loads |= other.loads
        self.stores |= other.stores; self.vcalls |= other.vcalls; self.normalcalls |= other.normalcalls
        self.formalargs |= other.formalargs; self.thisvars |= other.thisvars; self.heaptypes |= other.heaptypes
        self.actualargs |= other.actualargs; self.formalreturns |= other.formalreturns
        self.actualreturns |= other.actualreturns; self.lookups |= other.lookups
        self.class_names |= other.class_names

    def run(self): self.visit(self.tree)

    def current_MethId(self):
        for lookup in self.lookups:
            if lookup.class_type == self.enclosing_class and lookup.sig == self.current_func:
                return lookup.method_id
        raise Exception(f"No method ID found for class '{self.enclosing_class}' and function '{self.current_func}'")
    
    def _called_class_name(self, node):
        if not isinstance(node, ast.Call):
            return None
        func = node.func
        if isinstance(func, ast.Name) and func.id in self.class_names:
            return func.id
        if isinstance(func, ast.Attribute) and func.attr in self.class_names:
            return func.attr
        return None

    def visit_Assign(self, node):
        # x = y (move)
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, ast.Name)
        ):
            to_var = Var(node.targets[0].id)
            from_var = Var(node.value.id)
            move = Move(to_var, from_var)
            self.moves.add(move)

        # x = A(...) (alloc)
        cls = self._called_class_name(node.value)
        if (len(node.targets) == 1 
            and isinstance(node.targets[0], ast.Name) 
            and isinstance(node.value, ast.Call) 
            and cls):
            var = Var(node.targets[0].id)
            heap = Heap(get_attrs(node))
            in_meth = self.current_MethId()
            self.allocs.add(Alloc(var, heap, in_meth))
            self.heaptypes.add(HeapType(heap, ClassType(cls)))

        # x = f(...) (normal function call)
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id not in self.class_names
        ):
            # add NormalCall
            f_sig = Sig(node.value.func.id)
            in_meth = self.current_MethId()
            to_var = Var(node.targets[0].id)
            callsite = CallSite(get_attrs(node))
            normalcall = NormalCall(f_sig, callsite, in_meth)
            self.normalcalls.add(normalcall)
            # add ActualArg, ActualReturn
            for idx, arg in enumerate(node.value.args):
                if isinstance(arg, ast.Name):
                    self.actualargs.add(ActualArg(callsite, idx, Var(arg.id)))
            self.actualreturns.add(ActualReturn(callsite, to_var))

        # x = y.f (Load)
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, ast.Attribute)
            and isinstance(node.value.value, ast.Name) # y is a variable
        ):
            to_var = Var(node.targets[0].id)
            base_var = Var(node.value.value.id)
            field = Field(node.value.attr)
            load = Load(to_var, base_var, field)
            self.loads.add(load)

        # x.f = y (Store)
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Attribute)
            and isinstance(node.targets[0].value, ast.Name)
            and isinstance(node.value, ast.Name)
        ):
            base_var = Var(node.targets[0].value.id)
            field = Field(node.targets[0].attr)
            from_var = Var(node.value.id)
            store = Store(base_var, field, from_var)
            self.stores.add(store)

        # x = y.f(...) (VCall)
        if (
            len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Attribute)
            and isinstance(node.value.func.value, ast.Name)
        ):
            base_var = Var(node.value.func.value.id) # y 
            signature = Sig(node.value.func.attr) # f 
            callsite = CallSite(get_attrs(node))
            in_meth = self.current_MethId()
            vcall = VCall(base_var, signature, callsite, in_meth)
            self.vcalls.add(vcall)
            # add ActualArg, ActualReturn
            to_var = Var(node.targets[0].id)
            for idx, arg in enumerate(node.value.args):
                if isinstance(arg, ast.Name):
                    self.actualargs.add(ActualArg(callsite, idx, Var(arg.id)))
            self.actualreturns.add(ActualReturn(callsite, to_var))
            
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        prev_func = self.current_func
        self.current_func = Sig(node.name)

        methid = self.current_MethId()
        args = node.args
        arg_names = [a.arg for a in args.args]  

        # add ThisVar
        if self.enclosing_class and self.enclosing_class != global_class_type and arg_names:
            this_var = Var(arg_names[0])
            self.thisvars.add(ThisVar(methid, this_var))           
            arg_names = arg_names[1:]

        # add FormalArg
        for idx, name in enumerate(arg_names):
            fa = FormalArg(methid, idx, Var(name))
            self.formalargs.add(fa)

        # add FormalReturn
        for stmt in node.body:
            for ret in ast.walk(stmt):
                if isinstance(ret, ast.Return) and isinstance(ret.value, ast.Name):
                    self.formalreturns.add(FormalReturn(methid, Var(ret.value.id)))

        self.generic_visit(node)
        self.current_func = prev_func


    def visit_ClassDef(self, node):
        prev_class = self.enclosing_class
        self.enclosing_class = ClassType(node.name)
        self.generic_visit(node)
        self.enclosing_class = prev_class
        
    def print(self):
        for s in [self.allocs, self.moves, self.loads, self.stores, self.vcalls, self.normalcalls,
                  self.formalargs, self.thisvars, self.heaptypes, self.actualargs,
                  self.formalreturns, self.actualreturns, self.lookups]:
            for x in s: print(x)

####################################################

class CallNormalizer(ast.NodeTransformer):
    def __init__(self):
        self.counter = 0
        self.temp_assignments = []

    def _new_temp(self):
        self.counter += 1
        return f"t{self.counter}"

    def visit_Expr(self, node):
        self.generic_visit(node)
        return self._maybe_wrap_with_temps(node)

    def visit_Assign(self, node):
        self.generic_visit(node)
        return self._maybe_wrap_with_temps(node)

    def _maybe_wrap_with_temps(self, node):
        if self.temp_assignments:
            temp_nodes = self.temp_assignments
            self.temp_assignments = []
            return temp_nodes + [node]
        return node

    def visit_Call(self, node):
        self.generic_visit(node)

        new_args = []
        for arg in node.args:
            if isinstance(arg, ast.Call):
                temp_var = self._new_temp()
                assign = ast.Assign(
                    targets=[ast.Name(id=temp_var, ctx=ast.Store())],
                    value=arg
                )
                ast.copy_location(assign, arg)
                self.temp_assignments.append(assign)
                new_args.append(ast.copy_location(ast.Name(id=temp_var, ctx=ast.Load()), arg))
            else:
                new_args.append(arg)

        new_call = ast.Call(func=node.func, args=new_args, keywords=node.keywords)
        ast.copy_location(new_call, node)

        temp_var = self._new_temp()
        assign = ast.Assign(
            targets=[ast.Name(id=temp_var, ctx=ast.Store())],
            value=new_call
        )
        ast.copy_location(assign, node)
        self.temp_assignments.append(assign)

        return ast.copy_location(ast.Name(id=temp_var, ctx=ast.Load()), node)

def normalize(tree):
    normalizer = CallNormalizer()

    new_body = []
    for stmt in tree.body:
        result = normalizer.visit(stmt)
        if isinstance(result, list):
            new_body.extend(result)
        else:
            new_body.append(result)

    tree.body = new_body

    tree = ast.fix_missing_locations(tree)

    return tree

####################################################

def empty_ctx():
    return "e"

def record(heap, ctx):
    return empty_ctx()

def merge(heap, hctx, invo, ctx):
    return invo

class Solver():
    def __init__(self, collector):
        self.collector = collector
        self.var_points_to = {}
        self.field_points_to = {}
        self.inter_proc_assign = {}
        self.call_graph = {}
        self.reachable = {}
        self.reachable[global_method_id] = set(empty_ctx())  # Global method is reachable 
        self.method_call_graph = defaultdict(set)

    def get_allocs(self, meth):
        allocs = []
        for alloc in self.collector.allocs:
            if alloc.meth == meth:
                allocs.append(alloc)
        return allocs
    
    def transfer_alloc(self):
        for meth, ctxs in self.reachable.items():
            for ctx in ctxs:
                allocs = self.get_allocs(meth)
                for alloc in allocs:
                    var = alloc.var 
                    heap = alloc.heap 
                    hctx = record(heap, ctx)
                    self.var_points_to.setdefault((var, ctx), set()).add((heap, hctx))

    def transfer_move(self):
        for move in self.collector.moves:
            to = move.to_var
            from_ = move.from_var
            tuples = []
            for (var, ctx), points_to_set in self.var_points_to.items():
                if var == from_:
                    for heap, hctx in points_to_set:
                        tuples.append((from_, ctx, heap, hctx))
            for (_, ctx, heap, hctx) in tuples:
                if (to, ctx) not in self.var_points_to:
                    self.var_points_to.setdefault((to, ctx), set()).add((heap, hctx))
                else:
                    points_to_set = self.var_points_to[(to, ctx)]
                    points_to_set.add((heap, hctx))
                    self.var_points_to.setdefault((to, ctx), points_to_set)

    def transfer_load(self):
        for load in self.collector.loads:
            to_var = load.to_var
            base_var = load.base_var
            field = load.field

            for (var, ctx), points_to_set in list(self.var_points_to.items()):
                if var != base_var:
                    continue
                for base_heap, base_hctx in points_to_set:
                    key = (base_heap, base_hctx, field)
                    if key not in self.field_points_to:
                        continue
                    for heap, hctx in self.field_points_to[key]:
                        self.var_points_to.setdefault((to_var, ctx), set()).add((heap, hctx))

    def transfer_arg(self):
        for (invo_site, caller_ctx), callees in self.call_graph.items():
            for callee_meth, callee_ctx in callees:
                formal_args = [
                    fa for fa in self.collector.formalargs
                    if fa.method_id == callee_meth
                ]
                for fa in formal_args:
                    idx = fa.index
                    to_var = fa.var

                    for aa in self.collector.actualargs:
                        if aa.callsite == invo_site and aa.index == idx:
                            from_var = aa.var
                            self.inter_proc_assign.setdefault((to_var, callee_ctx), set()).add((from_var, caller_ctx))

    def transfer_store(self):
        for store in self.collector.stores:
            base_var = store.base_var
            field = store.field
            from_var = store.from_var

            for (var, ctx), from_pts in list(self.var_points_to.items()):
                if var != from_var:
                    continue

                base_pts = self.var_points_to.get((base_var, ctx), set())

                for from_heap, from_hctx in from_pts:
                    for base_heap, base_hctx in base_pts:
                        key = (base_heap, base_hctx, field)
                        self.field_points_to.setdefault(key, set()).add((from_heap, from_hctx))

    def transfer_ret(self):
        for (invo_site, caller_ctx), callees in self.call_graph.items():
            for callee_meth, callee_ctx in callees:
                formal_rets = [
                    fr.var for fr in self.collector.formalreturns
                    if fr.method_id == callee_meth
                ]

                actual_ret_vars = [
                    ar.var for ar in self.collector.actualreturns
                    if ar.callsite == invo_site
                ]

                for from_var in formal_rets:
                    for to_var in actual_ret_vars:
                        self.inter_proc_assign.setdefault((to_var, caller_ctx), set()).add((from_var, callee_ctx))

    def transfer_interproc(self):
        for (to_var, to_ctx), from_pairs in list(self.inter_proc_assign.items()):
            for from_var, from_ctx in from_pairs:
                pts = self.var_points_to.get((from_var, from_ctx), set())
                for heap, hctx in pts:
                    self.var_points_to.setdefault((to_var, to_ctx), set()).add((heap, hctx))

    def transfer_vcall(self):
        for vcall in self.collector.vcalls:
            base_var = vcall.base_var
            sig = vcall.signature
            callsite = vcall.callsite
            caller_meth = vcall.mid

            caller_ctxs = self.reachable.get(caller_meth, set())

            for caller_ctx in caller_ctxs:
                base_pts = self.var_points_to.get((base_var, caller_ctx), set())
                for heap, hctx in base_pts:
                    heaptypes = [
                        ht.class_type for ht in self.collector.heaptypes
                        if ht.heap == heap
                    ]
                    for class_type in heaptypes:
                        for lookup in self.collector.lookups:
                            if lookup.class_type == class_type and lookup.sig == sig:
                                callee_meth = lookup.method_id
                                this_vars = [
                                    tv.var for tv in self.collector.thisvars
                                    if tv.method_id == callee_meth
                                ]
                                if not this_vars:
                                    continue  # no self variable
                                this_var = this_vars[0]
                                callee_ctx = merge(heap, hctx, callsite, caller_ctx)
                                self.var_points_to.setdefault((this_var, callee_ctx), set()).add((heap, hctx))
                                self.reachable.setdefault(callee_meth, set()).add(callee_ctx)
                                self.call_graph.setdefault((callsite, caller_ctx), set()).add((callee_meth, callee_ctx))

    def transfer_call(self):
        for call in self.collector.normalcalls:
            sig = call.func_name
            callsite = call.callsite
            caller_meth = call.mid

            caller_ctxs = self.reachable.get(caller_meth, set())

            callee_methods = [
                lookup.method_id for lookup in self.collector.lookups
                if lookup.class_type == global_class_type and lookup.sig == sig
            ]

            for caller_ctx in caller_ctxs:
                for callee_meth in callee_methods:
                    callee_ctx = merge(heap=None, hctx=None, invo=callsite, ctx=caller_ctx)
                    self.reachable.setdefault(callee_meth, set()).add(callee_ctx)
                    self.call_graph.setdefault((callsite, caller_ctx), set()).add((callee_meth, callee_ctx))


    def run(self):
        iteration = 0
        while True:
            iteration += 1
            print(f"--- Iteration {iteration} ---")

            old_var_points_to = self.var_points_to.copy()
            old_field_points_to = self.field_points_to.copy()
            old_inter_proc_assign = self.inter_proc_assign.copy()
            old_call_graph = self.call_graph.copy()
            old_reachable = {k: set(v) for k, v in self.reachable.items()}

            self.transfer_alloc()
            self.transfer_move()
            self.transfer_load()
            self.transfer_store()
            self.transfer_arg()
            self.transfer_ret() 
            self.transfer_interproc()
            self.transfer_vcall()
            self.transfer_call()

            if (
                old_var_points_to == self.var_points_to and
                old_field_points_to == self.field_points_to and
                old_inter_proc_assign == self.inter_proc_assign and
                old_call_graph == self.call_graph and
                old_reachable == self.reachable
            ):
                print("Reached fixpoint.")
                break


    def print(self):
        print("Variable Points-to:")
        for (var, ctx), points_to_set in self.var_points_to.items():
            print(f"  ({var}, {ctx}) -> {', '.join(str(pt) for pt in points_to_set)}")

        print("Field Points-to:")
        for (baseH, baseHCtx, fld), points_to_set in self.field_points_to.items():
            print(f"  ({baseH}, {baseHCtx}, {fld}) -> {', '.join(str(pt) for pt in points_to_set)}")

        print("Inter-procedural Assignments:")
        for to, from_pairs in self.inter_proc_assign.items():
            print(f"  {to} <- {from_pairs}")

        print("Call Graph:")
        for caller, callees in self.call_graph.items():
            print(f"  {caller} -> {callees}")

        print("Reachable Contexts:")
        for meth, ctxs in self.reachable.items():
            print(f"  {meth}: {ctxs}")

    def find_enclosing_function(self, callsite):
        for call in self.collector.normalcalls:
            if call.callsite == callsite:
                return call.mid
        for call in self.collector.vcalls:
            if call.callsite == callsite:
                return call.mid
        raise Exception(f"No mid found for {callsite}")
    
    def find_method_name(self, mid):
        for lookup in self.collector.lookups:
            if lookup.method_id == mid:
                return f"{lookup.class_type.name}.{lookup.sig.name}"
        raise Exception(f"No method name found for {mid}")
        
    def build_method_call_graph(self):
        for (callsite, caller_ctx), callees in self.call_graph.items():
            caller_mid = self.find_enclosing_function(callsite)
            for callee_mid, _ in callees:
                caller_name = self.find_method_name(caller_mid)
                callee_name = self.find_method_name(callee_mid)
                self.method_call_graph[caller_name].add(callee_name)
    
    def visualize_method_call_graph(self, filename="call_graph", format="pdf"):
        dot = graphviz.Digraph(format=format)
        dot.attr(rankdir="LR")  
        for caller, callees in self.method_call_graph.items():
            caller = f"{caller}"
            dot.node(caller)
            for callee in callees:
                callee = f"{callee}"
                dot.node(callee)
                dot.edge(caller, callee)

        output_path = dot.render(filename=filename, cleanup=True)
        print(f"Call graph written to: {output_path}")

####################################################

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <files to analyze>")
        sys.exit(1)

    merged_collector = Collector(ast.Module(body=[]))
    for filename in sys.argv[1:]:
        with open(filename, "r", encoding="utf-8") as f: code = f.read()
        tree = ast.parse(code)
        tree = normalize(tree)
        print(f"--- Normalized code for {filename} ---")
        print(astor.to_source(tree))
        collector = Collector(tree); collector.run()
        merged_collector.merge(collector)

    merged_collector.print()
    print("\nAnalysis complete. Running solver...")
    solver = Solver(merged_collector)
    solver.run(); solver.print()
    solver.build_method_call_graph()
    solver.visualize_method_call_graph(filename="call_graph", format="pdf")