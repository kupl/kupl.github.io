(*********************)
(* Problem 1: filter *)
(*********************)
let rec filter pred lst = [] (* TODO *)

(*********************)
(* Problem 2: zipper *)
(*********************)
let rec zipper : int list * int list -> int list
=fun (a,b) -> [] (* TODO *)

(*******************)
(* Problem 3: iter *)
(*******************)

let rec iter : int * (int -> int) -> (int -> int)
=fun (n,f) -> f (* TODO *)

(*********************)
(* Problem 4: Diff   *)
(*********************)
type aexp = 
  | Const of int 
  | Var of string 
  | Power of string * int 
  | Times of aexp list
  | Sum of aexp list

let rec diff : aexp * string -> aexp
=fun (aexp,x) -> aexp (* TODO *)

(*************************)
(* Problem 5: Calculator *)
(*************************)
type exp = X
         | INT of int
         | ADD of exp * exp
         | SUB of exp * exp
         | MUL of exp * exp
         | DIV of exp * exp
         | SIGMA of exp * exp * exp
let calculator : exp -> int
=fun e -> 0 (* TODO *)
