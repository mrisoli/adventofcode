module Data.Common
( Coordinate
, getCoordinate
, getDirection
) where

import Data.Maybe

type Coordinate = (Int, Int)
data Direction = Up | MRight | Down | MLeft

getCoordinate :: Coordinate -> Maybe Direction -> Coordinate
getCoordinate (h,v) (Just Up) = (h - 1, v)
getCoordinate (h,v) (Just MRight) = (h, v + 1)
getCoordinate (h,v) (Just MLeft) = (h, v - 1)
getCoordinate (h,v) (Just Down) = (h + 1, v)
getCoordinate c Nothing = c

getDirection :: Char -> Maybe Direction
getDirection '^' = Just Up
getDirection '>' = Just MRight
getDirection '<' = Just MLeft
getDirection 'v' = Just Down
getDirection _ = Nothing

