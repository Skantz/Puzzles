--import Control.Monad(replicateM)


--writeOutput = unlines . (map show) -- [1, 2] --> ["1", "2"] --> "1\n2\n"
--readInput = (map read) . words -- "1 2\n3 5\n" --> ["1", "2", "3", "5"] --> [1, 2, 3, 5]

main = do
    inp <- getContents

    let inp2 =  words inp :: [String]
    let inp3 = map (read::String->Int) inp2 :: [Int]
    let inp4 = head inp3 :: Int
    let inp5 = tail inp3 :: [Int]

    let ans  = solve (maximum inp5) inp5
    if ans == []
        then putStrLn "good job"
        else mapM_ putStrLn (map show ans)


solve :: Int -> [Int] -> [Int]
solve 0 x = []
solve n (x:xs)
        | elem n (x:xs) = solve (n - 1) (x:xs)
        | otherwise     = solve (n - 1) (x:xs) ++ [n] 

