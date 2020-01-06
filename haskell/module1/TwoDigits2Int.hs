import Data.Char
twoDigits2Int :: Char -> Char -> Int
twoDigits2Int x y | isDigit x && isDigit y = 10 * digitToInt x + digitToInt y
                  | otherwise = 100