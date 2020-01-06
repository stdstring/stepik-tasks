seqA :: Integer -> Integer
seqA 0 = 1
seqA 1 = 2
seqA 2 = 3
seqA n = let
             helper i n a2 a1 a0 | i == n = a2
             helper i n a2 a1 a0 | otherwise = helper (i + 1) n (a2 + a1 - 2 * a0) a2 a1
         in helper 2 n 3 2 1