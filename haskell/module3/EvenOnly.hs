evenOnly :: [a] -> [a]
evenOnly = reverse.fst.foldl (\(dest, index) x -> (if index `mod` 2 == 1 then dest else x : dest, 1 + index)) ([], 1)

evenOnly' :: [a] -> [a]
evenOnly' xs = foldr (\(x, idx) rest -> (if idx `rem` 2 == 1 then [] else [x]) ++ rest) [] (zip xs [1..])