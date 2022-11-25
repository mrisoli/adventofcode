import Data.Common

calc :: [Int] -> Int
calc [w, l, h] =
    let lw = l * w
        lh = l * h
        wh = w * h
    in (2 * lw) + (2 * lh) + (2 * wh) + (minimum [lw, lh, wh])

main = do
    contents <- getContents
    putStrLn $ solve calc contents
