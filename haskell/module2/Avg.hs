avg :: Int -> Int -> Int -> Double
avg n1 n2 n3 = (x1 + x2 + x3) / 3.0 where
    x1 = fromIntegral n1 :: Double
    x2 = fromIntegral n2 :: Double
    x3 = fromIntegral n3 :: Double