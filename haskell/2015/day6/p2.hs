import Data.Map (Map)
import qualified Data.Map as Map
import Data.Common

sub :: Int -> Int
sub 0 = 0
sub n = n - 1

updateCell :: Switch -> (Int -> Int)
updateCell On = (+1)
updateCell Off = sub
updateCell Toggle = (+2)

setCell :: Switch -> Int
setCell On = 1
setCell Off = 0
setCell Toggle = 2

cellTransform :: Switch -> Map Pos Int -> Pos -> Map Pos Int
cellTransform s m p
    | Map.member p m = Map.adjust (updateCell s) p m
    | otherwise = Map.insert p (setCell s) m

main = do
    contents <- getContents
    print $ solve contents Map.empty cellTransform (sum . Map.elems)
