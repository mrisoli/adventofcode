module Data.Common
( solve
) where

import Data.List.Split

wr :: ([Int] -> Int) -> [Char] -> Int
wr calc c = calc $ (map read) $ (splitOn "x") $ c

solve :: ([Int] -> Int) -> [Char] -> [Char]
solve calc c = show $ sum $ (map (wr calc)) $ (lines c)
