groupElems :: Eq a => [a] -> [[a]]
groupElems [] = []
groupElems [x] = [[x]]
groupElems (x: xs) = let dest@(gr : grs) = groupElems xs in if head gr == x then (x : gr) : grs else [x] : dest