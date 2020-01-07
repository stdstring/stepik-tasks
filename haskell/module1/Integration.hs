integration :: (Double -> Double) -> Double -> Double -> Double
integration f a b = h * (0.5 * (f a + f b) + innerSum 1 0) where
    n = 1000
    h = (b - a) / n
    innerSum i value | i == n = value
                     | otherwise = innerSum (i + 1) (value + f (a + i * h))