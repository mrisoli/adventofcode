import Text.Regex.Posix
import Data.Ix
import Data.Set (Set)
import qualified Data.Set as Set

type Pos = (Int, Int)

data Switch = On | Off | Toggle deriving(Show)
data Command = Command Switch [Pos] deriving(Show)

getSwitch :: [Char] -> Switch
getSwitch "turn off" = Off
getSwitch "turn on" = On
getSwitch "toggle" = Toggle

getOffset :: Pos -> Pos
getOffset (a,b) = (a + 1, b + 1)
getRange :: [Char] -> [Char] -> [Pos]
getRange x y =
     range (getOffset rx, getOffset ry)
     where rx = read ("(" ++ x ++ ")") ::(Pos)
           ry = read ("(" ++ y ++ ")") ::(Pos)

mkCommand :: [Char] -> Command
mkCommand s = do
    let (_,_,_, [cmd, xr, yr]) = s =~ "([a-z ]+) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)" :: (String, String, String, [String])
     in Command (getSwitch cmd) (getRange xr yr)

transformCell :: Switch -> Set Pos -> Pos -> Set Pos
transformCell On m p = Set.insert p m
transformCell Off m p = Set.delete p m
transformCell Toggle m p
    | Set.member p m = Set.delete p m
    | otherwise = Set.insert p m

transform :: Set.Set Pos -> Command -> Set.Set Pos
transform m (Command s p) = foldl (transformCell s) m p

getCommands :: [Char] -> [Command]
getCommands s = map mkCommand (lines s)

main = do
    contents <- getContents
    print $ Set.size $ foldl transform Set.empty (getCommands contents)
