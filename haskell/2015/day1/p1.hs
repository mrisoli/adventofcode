countPar :: [Char] -> Char -> Int
countPar str c = length $ filter (== c) str

solve :: [Char] -> [Char]
solve contents
    = show $ (countPar contents '(')  - (countPar contents ')')

main = do
    contents <- getContents
    putStrLn $ solve $ contents
