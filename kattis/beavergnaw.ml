#load "str.cma";;
open List
open String
open Float

let rec pow x n =
  match n with
    | 0 -> 1.0
    | _ -> x *. (pow x (n - 1))

let pi = acos (-.1.)
(*let pi = 3.1415926535897932384626433*)

let compute x y = ((x ** 3.) -. (6. *. y) /. pi) ** (1. /. 3.)

let rec main () =
  let inp = read_line () in
  let x_y = Str.split (Str.regexp " ") inp in
  let x = float_of_string (nth x_y 0) in
  let y = float_of_string (nth x_y 1) in
  match x, y with
    | 0., 0. -> ()
    | _, _ -> Printf.printf("%f\n") (compute x y); main ()

let () = main ()