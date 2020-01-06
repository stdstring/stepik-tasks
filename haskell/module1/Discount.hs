discount :: Double -> Double -> Double -> Double
discount limit proc sum | sum >= limit = sum * (100 - proc) / 100
                        | otherwise = sum

standardDiscount :: Double -> Double
standardDiscount = discount 1000 5