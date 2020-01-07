sumOdd :: [Integer] -> Integer
sumOdd = foldr (\x s -> if x `rem` 2 == 1 then x + s else s) 0