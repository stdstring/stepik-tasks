import Control.Monad.Writer.Lazy

type Shopping = Writer (Sum Integer) ()

purchase :: String -> Integer -> Shopping
purchase item cost = tell $ Sum cost

total :: Shopping -> Integer
total = getSum . execWriter

type Shopping' = Writer ([String], Sum Integer) ()

purchase' :: String -> Integer -> Shopping'
purchase' item cost = tell ([item], Sum cost)

total' :: Shopping' -> Integer
total' = getSum . snd . execWriter

items' :: Shopping' -> [String]
items' = fst . execWriter