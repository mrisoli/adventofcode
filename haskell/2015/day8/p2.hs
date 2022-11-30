convertPar :: Char -> Int
convertPar '(' = 1
convertPar ')' = -1
convertPar _ = 0

solve :: [Char] -> [Char]
solve
    str = show $ length $ takeWhile (>= 0) $ scanl (+) 0 (map convertPar str)

main = do
    contents <- getContents
    putStrLn $ solve $ contents
