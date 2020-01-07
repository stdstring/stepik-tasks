perms :: [a] -> [[a]]
perms [] = [[]]
perms [x] = [[x]]
perms (x:xs) = concatMap (insertElement x) (perms xs) where
    insertElement a [] = [[a]]
    insertElement a dest@(b:bs) = (a:dest) : map (b:) (insertElement a bs)

perms' :: [a] -> [[a]]
perms' [] = [[]]
perms' xs = permsImpl [] [] xs where
    permsImpl prefix lrest [] = []
    permsImpl prefix [] [current] = [current : prefix]
    permsImpl prefix lrest (current : rrest) = permsImpl prefix (lrest ++ [current]) rrest ++ (permsImpl (current : prefix) [] (lrest ++ rrest))