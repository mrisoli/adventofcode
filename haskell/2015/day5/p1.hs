import Text.Regex.Posix

hasThreeVowels :: [Char] -> Bool
hasThreeVowels s = s =~ "([a-z]*[aeiou][a-z]*){3,}"

checkConsecutive :: (Char, Char) -> Bool
checkConsecutive (a, b) = a == b

hasConsecutiveCharacters :: [Char] -> Bool
hasConsecutiveCharacters s = any checkConsecutive (zip s $ tail s)

noIllegalPairs :: [Char] -> Bool
noIllegalPairs s = not $ s =~ "(ab|cd|pq|xy)"

isNice :: [Char] -> Bool
isNice s = (hasThreeVowels s) && (hasConsecutiveCharacters s) && (noIllegalPairs s)

main = do
    contents <- getContents
    print $ length $ filter isNice (lines contents)
