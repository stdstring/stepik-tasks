lengthList :: [a] -> Int
lengthList = foldr (\_ s -> s + 1)  0