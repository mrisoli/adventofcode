import Data.Common
import qualified Data.Set as Set

navigate :: Coordinate -> Set.Set Coordinate -> [Char]  -> Set.Set Coordinate
navigate _ v [] = v
navigate c v (x:xs) =
    let newCoordinate = getCoordinate c (getDirection x)
     in navigate newCoordinate (Set.insert newCoordinate v) xs

solve :: [Char] -> [Char]
solve = show . Set.size . (navigate (0,0) $ Set.fromList [(0,0)])

main = do
    contents <- getContents
    putStrLn $ solve $ contents
