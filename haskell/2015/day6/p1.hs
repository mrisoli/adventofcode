import Data.Set (Set)
import qualified Data.Set as Set
import Data.Common

cellTransform :: Switch -> Set Pos -> Pos -> Set Pos
cellTransform On m p = Set.insert p m
cellTransform Off m p = Set.delete p m
cellTransform Toggle m p
    | Set.member p m = Set.delete p m
    | otherwise = Set.insert p m

main = do
    contents <- getContents
    print $ solve contents Set.empty cellTransform Set.size
