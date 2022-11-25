countAll :: [Char] -> Int
countAll c = sum $ map length $ lines c

replaceChars :: [Char] -> [Char]
replaceChars c = c

countValid :: [Char] -> Int
countValid c = sum $ map length $ replaceChars $ tail $ init $ lines c

solve :: [Char] -> [Char]
solve c
    = show $ countAll c - countValid c

main = do
    contents <- getContents
    putStrLn $ solve contents
