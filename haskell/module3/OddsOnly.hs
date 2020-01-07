oddsOnly :: Integral a => [a] -> [a]
oddsOnly [] = []
oddsOnly (x : xs) | odd x == True = x : oddsOnly xs
oddsOnly (x : xs) | otherwise = oddsOnly xs