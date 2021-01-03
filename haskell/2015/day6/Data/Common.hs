module Data.Common
( Pos
, Switch (On, Off, Toggle)
, Transform
, solve
) where

import Text.Regex.Posix
import Data.Ix

type Transform a = (a -> CellToggle -> a)
type Pos = (Int, Int)
type CellToggle = (Switch, Pos)

data Switch = On | Off | Toggle
data Command = Command Switch [Pos]

getSwitch :: [Char] -> Switch
getSwitch "turn off" = Off
getSwitch "turn on" = On
getSwitch "toggle" = Toggle

getTuple :: [Char] -> Pos
getTuple s = read ("(" ++ s ++ ")") ::Pos

getRange :: [Char] -> [Char] -> [Pos]
getRange x y =
     range (getTuple x, getTuple y)

mkCommand :: [Char] -> Command
mkCommand s = do
    let (_,_,_, [cmd, xr, yr]) = s =~ "([a-z ]+) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)" :: (String, String, String, [String])
     in Command (getSwitch cmd) (getRange xr yr)

getCommands :: [Char] -> [Command]
getCommands s = map mkCommand (lines s)

getToggles :: Command -> [CellToggle]
getToggles (Command c ps) = map (\x -> (c, x)) ps

transform :: Transform a -> a -> Command -> a
transform fn m c = foldl fn m (getToggles c)

solve :: a -> Transform a -> [Char] -> a
solve a fn c = foldl (transform fn) a (getCommands c)
