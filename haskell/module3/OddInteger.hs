data Odd = Odd Integer deriving (Eq,Show)

instance Enum Odd where
    succ (Odd a) = Odd (a + 2) 
    pred (Odd a) = Odd (a - 2) 
    toEnum idx = Odd (2 * (toInteger idx) + 1)
    fromEnum (Odd a) = fromInteger ((a - 1) `div` 2)
    enumFrom x = enumDeltaOdd x 2
    enumFromThen x@(Odd a) (Odd b) = enumDeltaOdd x (b - a)
    enumFromTo x lim = enumDeltaToOdd x 2 lim
    enumFromThenTo x@(Odd a) (Odd b) lim = enumDeltaToOdd x (b - a) lim

enumDeltaOdd x@(Odd a) d = x `seq` (x : enumDeltaOdd (Odd $ a + d) d)

enumDeltaToOdd x delta lim | delta >= 0 = up_list x delta lim
                           | otherwise  = dn_list x delta lim

up_list x0 delta (Odd lim) = go x0 where
    go x@(Odd value) | value > lim   = []
                     | otherwise = x : go (Odd $ value + delta)

dn_list x0 delta (Odd lim) = go x0 where
    go x@(Odd value) | value < lim   = []
                     | otherwise = x : go (Odd $ value + delta)