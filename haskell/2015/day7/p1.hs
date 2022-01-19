import Solution (getAns, calcCircuits, parseData)

solve :: [[Char]] -> Int
solve = getAns . calcCircuits . parseData

main = do
    contents <- getContents
    print $ solve $ lines $ contents
