(*#load "str.cma";;*)
open List
open String

let rec pow x n =
  match n with
    | 0 -> 1.0
    | _ -> x *. (pow x (n - 1))

let pi = acos (-1.)
let inp = read_line ()
let x_y = Str.split (Str.regexp " ") inp
let x = float_of_string (nth x_y 0)
let y = float_of_string (nth x_y 1)

let () =
match (pow y 2) /. (4.0 *. pi) >= x with
  | true  -> Printf.printf("%s") "Diablo is happy!"
  | false -> Printf.printf("%s") "Need more materials!"