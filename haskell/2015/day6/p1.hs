import Data.Set (Set)
import qualified Data.Set as Set
import Data.Common

cellTransform :: Transform (Set Pos)
cellTransform m (On, p) = Set.insert p m
cellTransform m (Off, p) = Set.delete p m
cellTransform m (Toggle, p)
    | Set.member p m = Set.delete p m
    | otherwise = Set.insert p m

main = do
    contents <- getContents
    print $ Set.size $ solve Set.empty cellTransform contents
