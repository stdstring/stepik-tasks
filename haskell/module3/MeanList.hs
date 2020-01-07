meanList :: [Double] -> Double
meanList xs = sum / count where
    (sum, count) = foldr (\x (s, c) -> (x + s, 1 + c)) (0, 0) xs