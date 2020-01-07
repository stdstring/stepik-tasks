qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort [x] = [x]
qsort [x, y] = if x <= y then [x, y] else [y, x]
qsort xs@(x:_) = (qsort lxs) ++ exs ++ (qsort gxs) where
    lxs = filter (<x) xs
    exs = filter (==x) xs
    gxs = filter (>x) xs