data Shape = Circle Double | Rectangle Double Double

area :: Shape -> Double
area (Circle r) = pi * r ^ 2
area (Rectangle x y) = x * y

square :: Double -> Shape
square a = Rectangle a a

isSquare :: Shape -> Bool
isSquare (Rectangle x y) | x == y = True
isSquare _ | otherwise = False