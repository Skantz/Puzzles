let rec is_prime n i =
  if n < 2 then false
  if n <= 2 then true
    else if i = 1 then true
    else
      match (n mod i = 0) with
      | true -> false
      | false -> is_prime n (i - 1)

let sqrt_int n =
  let rec loop i =
    match (i * i > n) with
    | true -> i
    | false -> loop (i + 1)
  in loop 1

let rec loop n i sum =
  if n >= 2000000 then sum
  else
    match (is_prime n (sqrt_int n)) with
    | true -> (loop (n + 1) (i + 1) (sum + n))
    | false -> loop (n + 1) i sum

let main = Stdlib.print_int (loop 2 0 0)
 
