import Data.List.Split
import Data.List

calc :: [Int] -> Int
calc s =
    let [w, h] = drop 1 (reverse $ sort s)
    in (2 * w) + (2 * h) + (product s)

wr :: [Char] -> Int
wr = calc . (map read) . (splitOn "x")

solve :: [Char] -> [Char]
solve = show . sum . (map wr) . lines

main = do
    contents <- getContents
    putStrLn $ solve $ contents
