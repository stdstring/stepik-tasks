import Data.List(unfoldr)

revRange :: (Char,Char) -> [Char]
revRange = unfoldr g 
    where g (from, current) = if current < from then Nothing else Just (current, (from, pred current))