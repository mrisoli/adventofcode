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

cellTransform :: Transform (Map Pos Int)
cellTransform m (s, p)
    | Map.member p m = Map.adjust (updateCell s) p m
    | otherwise = Map.insert p (setCell s) m

main = do
    contents <- getContents
    print $ sum $ Map.elems $ solve Map.empty cellTransform contents
