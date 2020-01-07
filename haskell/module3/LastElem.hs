lastElem :: [a] -> a
lastElem = foldl1 (\_ x -> x)