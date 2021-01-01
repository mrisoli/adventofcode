import qualified Data.ByteString.Char8 as B
import qualified Crypto.Hash.MD5 as MD5
import Data.Char (isSpace)
import Data.Text as T
import Text.Hex (encodeHex)

trim :: String -> String
trim = f . f
        where f = Prelude.reverse . Prelude.dropWhile isSpace

encode :: String -> Int -> Text
encode s i = encodeHex $ MD5.hash $ B.pack $ s ++ (show i)

isValid :: Text -> Bool
isValid c = T.isPrefixOf (pack "000000") c

findResult :: String -> Int -> Int
findResult s i
  | isValid (encode s i) = i
  | otherwise = findResult s (i + 1)

main = do
        contents <- getContents
        print $ findResult (trim contents) 1
