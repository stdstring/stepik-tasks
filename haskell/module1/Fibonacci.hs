fibonacci :: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci (-1) = 1
fibonacci n | n < -1 = fibonacci (n + 2) - fibonacci (n + 1)
            | otherwise = fibonacci (n - 1) + fibonacci (n - 2)

fibonacci' :: Integer -> Integer
fibonacci' n = helper 0 1 n where
    helper current prev 0 = current
    helper current prev n | n > 0 = helper (current + prev) current (n - 1)
                          | n < 0 = helper (prev - current) current (n + 1)