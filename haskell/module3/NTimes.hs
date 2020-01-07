nTimes:: a -> Int -> [a]
nTimes _ 0 = []
nTimes elem n = elem : nTimes elem (n - 1)