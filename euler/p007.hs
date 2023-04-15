isPrime :: Int -> Int -> Bool
isPrime n 1 = True
isPrime n i =
  mod n i /= 0 && isPrime n (i - 1)

integerSquareRoot :: Int -> Int
integerSquareRoot n = floor (sqrt (fromIntegral n))

main :: IO ()
main = do
  let primesb = (\x -> isPrime x (integerSquareRoot x))
  let primes = filter primesb [2..]
  let nthPrime = primes !! 10000
  print nthPrime