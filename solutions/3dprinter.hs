main = do
  input <- getLine
  let number = head (map (read::String->Double) (words input) )
  let answer = solve number
  print answer

solve number
  |number == 1.0 = 1
  |otherwise = ( ceiling (logBase 2 number ) ) + 1

