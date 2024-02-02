module D1
( solve
, mappings
) where

import Text.Regex.TDFA
import Data.Readfile
import qualified Data.Map as M
import Debug.Trace

mappings :: M.Map String String
mappings = M.fromList [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")]

pattern :: String -> String
pattern "" = "([[:digit:]])"
pattern re = "([[:digit:]]|" ++ re ++ ")"

firstDigit :: String -> String -> String
firstDigit re s = s =~ (pattern re) :: String

lastDigit :: String -> String -> String
lastDigit re s = (reverse s) =~ (pattern $ reverse re) :: String

translate :: String -> String
translate s = M.findWithDefault s s mappings
firstLastDigits :: String -> String -> Int
firstLastDigits re s = read (translate (firstDigit re s) ++ translate (lastDigit re s)):: Int

mapOverList :: String -> [String] -> String
mapOverList re l = show . sum . map (firstLastDigits re) $ l

solve :: String -> IO ()
solve re = run (mapOverList re) 1
