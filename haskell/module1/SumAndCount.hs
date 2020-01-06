sum'n'count :: Integer -> (Integer, Integer)
sum'n'count 0 = (0, 1)
sum'n'count x | x < 0 = helper (-x) 0 0
              | otherwise = helper x 0 0
    where
        helper 0 sum count = (sum, count)
        helper n sum count = helper (div n 10) (sum + mod n 10) (count + 1)