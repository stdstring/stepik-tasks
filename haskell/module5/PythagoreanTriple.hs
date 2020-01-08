pythagoreanTriple :: Int -> [(Int, Int, Int)]
pythagoreanTriple x | x < 0 = []
pythagoreanTriple x = do
    c <- [1 .. x]
    b <- [1 .. (c - 1)]
    a <- [1 .. (b - 1)]
    if (a^2 + b^2) == (c^2) then [True] else []
    return (a, b, c)