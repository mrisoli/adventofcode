import Data.Common
import Data.List

calc :: [Int] -> Int
calc s =
    let [w, h] = drop 1 (reverse $ sort s)
    in (2 * w) + (2 * h) + (product s)

main = do
    contents <- getContents
    putStrLn $ (solve calc) $ contents
