import Data.Char(isDigit)

findDigit :: [Char] -> Maybe Char
findDigit [] = Nothing
findDigit (ch : chs) | isDigit ch = Just ch
                     | otherwise = findDigit chs

findDigitOrX :: [Char] -> Char
findDigitOrX chs =
    case findDigit chs of
        Just ch -> ch
        Nothing -> 'X'