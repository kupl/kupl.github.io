type a = Ptr of p | Int of int | Add of a * a | Nil
and  p = Var of var | Cdr of var
and  b = True | False | Not of b | And of b * b | Equal of a * a | IsNil of p
and  stmt = Assign of p * a | Skip | Seq of stmt list | If of b * stmt * stmt | While of b * stmt | Malloc of p
and var = string

(*
Example program:
malloc t1;
t1.cdr := Nil;
malloc t2;
t2.cdr := t1;
malloc t3;
t3.cdr := t2;
x := t3;
t1 := Nil;
t2 := Nil;
t3 := Nil;
y := Nil;
while (not is-nil(x)) do
  (z:=y; y:=x; x:=x.cdr; y.cdr:=z);
z:=nil
*)
let pgm =
    Seq [
      Malloc (Var "t1");
      Assign (Cdr "t1", Nil);
      Malloc (Var "t2");
      Assign (Cdr "t2", Ptr (Var "t1"));
      Malloc (Var "t3");
      Assign (Cdr "t3", Ptr (Var "t2"));
      Assign (Var "x", Ptr (Var "t3"));
      Assign (Var "t1", Nil);
      Assign (Var "t2", Nil);
      Assign (Var "t3", Nil);
      Assign (Var "y", Nil);
      While (Not (IsNil (Var "x")),
        Seq [
          Assign (Var "z", Ptr (Var "y"));
          Assign (Var "y", Ptr (Var "x"));
          Assign (Var "x", Ptr (Cdr "x"));
          Assign (Cdr "y", Ptr (Var "z"));
        ]
      );
      Assign (Var "z", Nil)
    ]

let analysis stmt = 0 (* Placeholder *)
