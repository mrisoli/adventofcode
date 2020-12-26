import Data.List.Split

calc :: [Int] -> Int
calc [w, l, h] =
    let lw = l * w
        lh = l * h
        wh = w * h
    in (2 * lw) + (2 * lh) + (2 * wh) + (minimum [lw, lh, wh])

wr :: [Char] -> Int
wr = calc . (map read) . (splitOn "x")

solve :: [Char] -> [Char]
solve = show . sum . (map wr) . lines

main = do
    contents <- getContents
    putStrLn $ solve $ contents
