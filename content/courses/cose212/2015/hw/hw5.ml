(*********************************************)
(* HW5: A Sound Static Type Checker for PROC *)
(*********************************************)

type exp = 
  | CONST of int
  | VAR of var
  | ADD of exp * exp
  | SUB of exp * exp
  | ISZERO of exp
  | IF of exp * exp * exp
  | LET of var * exp * exp
  | PROC of var * exp
  | CALL of exp * exp
and var = string

(* raise this exception when the program is determined to be ill-typed *)
exception TypeError

(* type *)
type typ = TyInt | TyBool | TyFun of typ * typ | TyVar of tyvar
and tyvar = string

(* type equations are represented by a list of "equalities" (ty1 = ty2)  *)
type typ_eqn = (typ * typ) list

(* generate a fresh type variable *)
let tyvar_num = ref 0
let fresh_tyvar () = (tyvar_num := !tyvar_num + 1; (TyVar ("t" ^ string_of_int !tyvar_num)))

(* type environment : var -> type *)
module TEnv = struct
  type t = var -> typ
  let empty = fun _ -> raise (Failure "Type Env is empty")
  let extend (x,t) tenv = fun y -> if x = y then t else (tenv y)
  let find tenv x = tenv x
end

(* substitution *)
module Subst = struct
  type t = (tyvar * typ) list
  let empty = []
  let find x subst = List.assoc x subst

  (* walk through the type, replacing each type variable by its binding in the substitution *)
  let rec apply : typ -> t -> typ
  =fun typ subst ->
    match typ with
    | TyInt -> TyInt
    | TyBool -> TyBool 
    | TyFun (t1,t2) -> TyFun (apply t1 subst, apply t2 subst)
    | TyVar x -> 
      try find x subst
      with _ -> typ

  (* add a binding (tv,ty) to the subsutition and propagate the information *)
  let extend tv ty subst = 
    (tv,ty) :: (List.map (fun (x,t) -> (x, apply t [(tv,ty)])) subst)
end

let rec gen_equations : TEnv.t -> exp -> typ -> typ_eqn 
=fun tenv e ty -> [] (* TODO *)

let solve : typ_eqn -> Subst.t
=fun eqn -> Subst.empty (* TODO *)

let typeof : exp -> typ 
=fun exp -> 
  let new_tv = fresh_tyvar () in
  let eqns = gen_equations TEnv.empty exp new_tv in
  let subst = solve eqns in
  let ty = Subst.apply new_tv subst in
    ty
