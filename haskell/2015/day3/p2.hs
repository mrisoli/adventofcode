import Data.Common
import qualified Data.Set as Set

type Pair = (Coordinate, Coordinate)
data Move = Santa | Robot deriving (Eq)

getPair :: Move -> Pair -> Char -> Pair

getPair Santa (s, r) c = (getCoordinate s (getDirection c), r)
getPair Robot (s, r) c = (s, getCoordinate r (getDirection c))

navigate :: Move -> Pair -> Set.Set Coordinate -> [Char]  -> Set.Set Coordinate
navigate _ _ v [] = v
navigate m p v (x:xs) =
    let newPair = getPair m p x
        newCoordinate = if m == Santa then fst newPair else snd newPair
        nextMove = if m == Santa then Robot else Santa
     in navigate nextMove newPair (Set.insert newCoordinate v) xs

solve :: [Char] -> [Char]
solve = show . Set.size . (navigate Santa ((0,0), (0,0)) $ Set.fromList [(0,0)])

main = do
    contents <- getContents
    putStrLn $ solve $ contents
