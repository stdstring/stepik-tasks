-- data Board = ...

-- nextPositions :: Board -> [Board]

nextPositionsN :: Board -> Int -> (Board -> Bool) -> [Board]
nextPositionsN b n pred | n < 0 = []
nextPositionsN b 0 pred = filter pred [b]
nextPositionsN b n pred = do
    position <- nextPositions b
    nextPositionsN position (n - 1) pred