import Data.Char

data Token = Number Int | Plus | Minus | LeftBrace | RightBrace deriving (Eq, Show)

asToken :: String -> Maybe Token
asToken "+" = Just Plus
asToken "-" = Just Minus
asToken "(" = Just LeftBrace
asToken ")" = Just RightBrace
asToken str | all isDigit str = let number = (read str :: Int) in Just $ Number number
asToken _ = Nothing

tokenize :: String -> Maybe [Token]
tokenize input = sequence $ map asToken $ words input