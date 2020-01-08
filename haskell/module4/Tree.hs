data Tree a = Leaf a | Node (Tree a) (Tree a)

height :: Tree a -> Int
height (Leaf _) = 0
height (Node left right) = 1 + max (height left) (height right)

size :: Tree a -> Int
size (Leaf _) = 1
size (Node left right) = 1 + (size left) + (size right)

avg :: Tree Int -> Int
avg t = let (c,s) = go t in s `div` c
    where
        go :: Tree Int -> (Int,Int)
        go (Leaf a) = (1, a)
        go (Node left right) = (c1 + c2, s1 + s2) where
            (c1, s1) = go left
            (c2, s2) = go right