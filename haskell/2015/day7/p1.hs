import Data.Map as Map
import Data.List.Split
import Data.List (isInfixOf)
import Data.Char (isDigit)
import Data.Bits

data AddrExp = ExpValue Int | Addr [Char] deriving (Show)
type ValuePair = (AddrExp, AddrExp)

data Operation = Not AddrExp | And ValuePair | Or ValuePair | Lshift ValuePair | Rshift ValuePair deriving (Show)
data Statement = StmtValue AddrExp | Op Operation
type Circuit = Map [Char] Statement
type Table = Map [Char] Int
type TableCircuit = (Table, Circuit)

mkV :: [Char] -> AddrExp
mkV c
  | all isDigit c = ExpValue (read c :: Int)
  | otherwise = (Addr c)

mkVP :: [Char] -> [Char] -> ValuePair
mkVP sp c =
    let [v1, v2] = splitOn sp c
     in (mkV v1, mkV v2)

parseStmt :: [Char] -> Statement
parseStmt s
    | isInfixOf "NOT" s =  Op (Not (mkV $ (splitOn " " s)!!1))
    | isInfixOf "AND" s =  Op (And (mkVP " AND " s))
    | isInfixOf "OR" s =  Op (Or (mkVP " OR " s))
    | isInfixOf "LSHIFT" s =  Op (Lshift (mkVP " LSHIFT " s))
    | isInfixOf "RSHIFT" s =  Op (Rshift (mkVP " RSHIFT " s))
    | otherwise = StmtValue (mkV s)

insertTC :: [Char] -> Statement -> TableCircuit -> TableCircuit
insertTC a (StmtValue (ExpValue i)) (t, c) = (insert a i t, insert a (StmtValue (ExpValue i)) c)
insertTC a s (t, c) = (t, insert a s c)

makeStmt :: [Char] -> TableCircuit -> TableCircuit
makeStmt r tc =
    let [stmt , address] = splitOn " -> " r
     in insertTC address (parseStmt stmt) tc

parseData :: [[Char]] -> TableCircuit
parseData = Prelude.foldr makeStmt (empty, empty)

gV :: Table -> AddrExp -> AddrExp
gV t (ExpValue v) = ExpValue v
gV t (Addr a) =
    let v = Map.lookup a t
     in case v of
          Just i -> ExpValue i
          Nothing -> Addr a

execOp :: (Int -> Int -> Int) -> ValuePair -> Operation -> Statement
execOp fn ((ExpValue v1), (ExpValue v2)) op = StmtValue (ExpValue (fn v1 v2))
execOp _ _ op = Op op

parseArgs :: Table -> ValuePair -> ValuePair
parseArgs t (v1, v2) = ((gV t v1), gV t v2)

runOp :: Table -> Operation -> Statement
runOp t (Not v) = execOp xor ((gV t v), ExpValue 65535) (Not v)
runOp t (And v) = execOp ((.&.)) (parseArgs t v) (And v)
runOp t (Or v) = execOp ((.|.)) (parseArgs t v) (Or v)
runOp t (Lshift v) = execOp (shiftL) (parseArgs t v) (Lshift v)
runOp t (Rshift v) = execOp (shiftR) (parseArgs t v) (Rshift v)

runSt :: Table -> Statement -> Statement
runSt t (StmtValue a) = StmtValue (gV t a)
runSt t (Op op) = runOp t op

transform :: [Char] -> Statement -> TableCircuit -> TableCircuit
transform a s (t, c) =
    let p = runSt t s
     in insertTC a p (t,c)

convert :: TableCircuit -> TableCircuit
convert (t, c) = foldrWithKey transform (t,c) c

calcCircuits :: TableCircuit -> Int
calcCircuits (t, c) =
    let v = Map.lookup "a" t
     in case v of
          Just i -> i
          Nothing -> calcCircuits $ convert (t, c)

solve :: [[Char]] -> Int
solve = calcCircuits . parseData

main = do
    contents <- getContents
    print $ solve $ lines $ contents
