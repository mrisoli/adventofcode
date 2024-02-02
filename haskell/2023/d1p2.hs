import D1
import Data.List
import qualified Data.Map as M

main :: IO ()
main = solve (intercalate "|" (M.keys mappings))
