import Data.List

main = do
  inp <- getLine
  let sequence = group (sort ((unwords . words) inp)) 
  if (length (head sequence) == length (last sequence)) then print 1
  else print 0
