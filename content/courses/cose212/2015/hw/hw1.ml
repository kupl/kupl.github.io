(* Problem 1 *)
let rec pascal : int * int -> int
=fun (x,y) -> 1 (* TODO *)

(* Problem 2 *)
let rec sigma : (int -> int) -> int -> int -> int
=fun f a b -> 1 (* TODO *)

(* Problem 3 *)
let rec max : int list -> int
=fun l -> 1 (* TODO *)

let rec min : int list -> int
=fun l -> 1 (* TODO *)

(* Problem 4 *)
type formula =
    True
  | False
  | Neg of formula
  | Or of formula * formula
  | And of formula * formula
  | Imply of formula * formula
  | Equiv of formula * formula

let rec eval : formula -> bool
=fun f -> true (* TODO *)

(* Problem 5 *)
type nat = ZERO | SUCC of nat

let rec natadd : nat -> nat -> nat
=fun n1 n2 -> ZERO(* TODO *)

let rec natmul : nat -> nat -> nat
=fun n1 n2 -> ZERO (* TODO *)
