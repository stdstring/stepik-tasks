data Coord a = Coord a a

distance :: Coord Double -> Coord Double -> Double
distance (Coord x1 y1) (Coord x2 y2) = sqrt ((x1 - x2) ^ 2 + (y1 - y2) ^ 2)

manhDistance :: Coord Int -> Coord Int -> Int
manhDistance (Coord x1 y1) (Coord x2 y2) = abs (x1 - x2) + abs (y1 - y2)

getCenter :: Double -> Coord Int -> Coord Double
getCenter size (Coord x y) = Coord xCenter yCenter where
    xCenter = (size * fromIntegral x) + (if x >= 0 then size/2 else -size/2)
    yCenter = (size * fromIntegral y) + (if y >= 0 then size/2 else -size/2)

getCell :: Double -> Coord Double -> Coord Int
getCell size (Coord x y) = Coord xCell yCell where
    xCell = truncate (x / size)
    yCell = truncate (y / size)