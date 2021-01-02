hasDoublePairs :: [Char] -> Bool
hasDoublePairs (f:s:xs)
    | length xs == 0 = False
    | elem (f,s) (zip xs $ tail xs) = True
    | otherwise = hasDoublePairs (s:xs)

hasLetterSeparator :: [(Char, Char)] -> Bool
hasLetterSeparator (f:s:xs)
    | fst f == snd s = True
    | length xs == 0 = False
    | otherwise = hasLetterSeparator (s:xs)

isNice :: [Char] -> Bool
isNice s = (hasDoublePairs s) && (hasLetterSeparator (zip s $ tail s))

main = do
    contents <- getContents
    print $ length $ filter isNice (lines contents)
