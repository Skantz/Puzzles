(*#load "str.cma";;*)

let rec sum_of_digits x =
  let bound = (x <= 0) in
  match bound with
    | true  -> 0
    | false -> (x mod 10) + (sum_of_digits (x / 10))

let rec iterate_until_true fn inp = 
  let evl = fn inp in
  match evl with
    | true  -> inp
    | false -> iterate_until_true fn (inp + 1)

let n = read_int ()
let ans = iterate_until_true (fun x -> (x mod (sum_of_digits x)) == 0) n
let p = Printf.printf("%d") ans

