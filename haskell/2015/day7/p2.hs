import Solution (getAns, calcCircuits, reset, parseData)

solve :: [[Char]] -> Int
solve cc =
    let d = parseData cc
        a = getAns $ calcCircuits d
     in getAns $ calcCircuits (reset d a)

main = do
    contents <- getContents
    print $ solve $ lines $ contents
