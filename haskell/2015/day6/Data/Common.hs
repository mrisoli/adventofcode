module Data.Common
( Pos
, Switch (On, Off, Toggle)
, solve
) where

import Text.Regex.Posix
import Data.Ix

type Pos = (Int, Int)

data Switch = On | Off | Toggle deriving(Show)
data Command = Command Switch [Pos] deriving(Show)

getSwitch :: [Char] -> Switch
getSwitch "turn off" = Off
getSwitch "turn on" = On
getSwitch "toggle" = Toggle

getTuple :: [Char] -> Pos
getTuple s = read ("(" ++ s ++ ")") ::(Pos)

getRange :: [Char] -> [Char] -> [Pos]
getRange x y =
     range (getTuple x, getTuple y)

mkCommand :: [Char] -> Command
mkCommand s = do
    let (_,_,_, [cmd, xr, yr]) = s =~ "([a-z ]+) ([0-9]+,[0-9]+) through ([0-9]+,[0-9]+)" :: (String, String, String, [String])
     in Command (getSwitch cmd) (getRange xr yr)

getCommands :: [Char] -> [Command]
getCommands s = map mkCommand (lines s)

transform :: (Switch -> a -> Pos -> a) -> a -> Command -> a
transform fn m (Command s p) = foldl (fn s) m p

solve :: [Char] -> a -> (Switch -> a -> Pos -> a) -> (a -> Int) -> Int
solve c a fn count = count $ foldl (transform fn) a (getCommands c)
