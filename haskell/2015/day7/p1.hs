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

mkValue :: [Char] -> AddrExp
mkValue c
  | all isDigit c = ExpValue (read c :: Int)
  | otherwise = (Addr c)

getValuePair :: [Char] -> [Char] -> ValuePair
getValuePair sp c =
    let [v1, v2] = splitOn sp c
     in (mkValue v1, mkValue v2)

parseStmt :: [Char] -> Statement
parseStmt s
    | isInfixOf "NOT" s =  Op (Not (mkValue $ (splitOn " " s)!!1))
    | isInfixOf "AND" s =  Op (And (getValuePair " AND " s))
    | isInfixOf "OR" s =  Op (Or (getValuePair " OR " s))
    | isInfixOf "LSHIFT" s =  Op (Lshift (getValuePair " LSHIFT " s))
    | isInfixOf "RSHIFT" s =  Op (Rshift (getValuePair " RSHIFT " s))
    | otherwise = StmtValue (mkValue s)

getStmt :: [Char] -> ([Char], Statement)
getStmt r =
    let [stmt , address] = splitOn " -> " r
     in (address, (parseStmt stmt))

insertIntoTblCircuit :: [Char] -> Statement -> TableCircuit -> TableCircuit
insertIntoTblCircuit a (StmtValue (ExpValue i)) (t, c) = (insert a i t, insert a (StmtValue (ExpValue i)) c)
insertIntoTblCircuit a s (t, c) = (t, insert a s c)

makeStmt :: [Char] -> TableCircuit -> TableCircuit
makeStmt r tc =
    let (address, stmt) = getStmt r
     in insertIntoTblCircuit address stmt tc

parseData :: [[Char]] -> TableCircuit
parseData = Prelude.foldr makeStmt (empty, empty)

addToTable :: [Char] -> Int -> Table -> Table
addToTable a i t = insert a i t

updateTc :: [Char] -> [Char] -> Table -> Circuit -> TableCircuit
updateTc a e t c
    | member e t = (insert a (t ! e) t, insert a (StmtValue (ExpValue (t ! e))) c)
    | otherwise = (t, insert a (StmtValue (Addr e)) c)

valueOrAddr :: Table -> AddrExp -> AddrExp
valueOrAddr t (ExpValue v) = ExpValue v
valueOrAddr t (Addr a)
    | member a t = ExpValue (t ! a)
    | otherwise = Addr a

processNot :: AddrExp ->  Statement
processNot (ExpValue v) = StmtValue (ExpValue (xor 65535 v))
processNot a = Op (Not a)

execOp :: (Int -> Int -> Int) -> ValuePair -> Operation -> Statement
execOp fn ((ExpValue v1), (ExpValue v2)) op = StmtValue (ExpValue (fn v1 v2))
execOp _ _ op = Op op

processOp :: Table -> Operation -> Statement
processOp t (Not v) = processNot (valueOrAddr t v)
processOp t (And (v1, v2)) = execOp ((.&.)) ((valueOrAddr t v1), (valueOrAddr t v2)) (And (v1, v2))
processOp t (Or (v1, v2)) = execOp ((.|.)) ((valueOrAddr t v1), (valueOrAddr t v2)) (Or (v1, v2))
processOp t (Lshift (v1, v2)) = execOp (shiftL) ((valueOrAddr t v1), (valueOrAddr t v2)) (Lshift (v1, v2))
processOp t (Rshift (v1, v2)) = execOp (shiftR) ((valueOrAddr t v1), (valueOrAddr t v2)) (Rshift (v1, v2))

processStmt :: Table -> Statement -> Statement
processStmt t (StmtValue a) = StmtValue (valueOrAddr t a)
processStmt t (Op op) = processOp t op

transform :: [Char] -> Statement -> TableCircuit -> TableCircuit
transform a s (t, c) =
    let p = processStmt t s
     in case p of
          (StmtValue (ExpValue i)) -> (addToTable a i t, c)
          (StmtValue (Addr e)) -> updateTc a e t c
          _ -> (t, insert a p c)

runStmts :: TableCircuit -> TableCircuit
runStmts (t, c) = foldrWithKey transform (t,c) c

calcCircuits :: TableCircuit -> Int
calcCircuits (t, c) =
    let v = Map.lookup "a" t
     in case v of
          Just i -> i
          Nothing -> calcCircuits $ runStmts (t, c)

solve :: [[Char]] -> Int
solve = calcCircuits . parseData

main = do
    contents <- getContents
    print $ solve $ lines $ contents
