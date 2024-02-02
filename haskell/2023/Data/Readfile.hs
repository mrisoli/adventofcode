module Data.Readfile
( run
) where

import Text.Read
import System.Environment
import System.IO

readFileContents :: FilePath -> IO [String]
readFileContents path = do
  contents <- readFile path
  return (lines contents)

addExtraArg :: Maybe Int -> String
addExtraArg v =
  case v of
    Nothing -> ".in"
    Just n -> "-" ++ show n ++ ".in"

getFilePath :: Int -> [String] -> FilePath
getFilePath n args = do
  let baseString = "inputs/"
  case args of
    [inputArg] ->
      baseString ++ "t" ++ show n ++ addExtraArg (readMaybe inputArg :: Maybe Int)
    _ -> baseString ++ "i" ++ show n ++ ".in"

run :: ([String] -> String) -> Int -> IO ()
run fn n = do
  args <- getArgs
  contents <- readFileContents (getFilePath n args)
  putStrLn (fn contents)
