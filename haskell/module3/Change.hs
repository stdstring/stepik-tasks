change :: (Ord a, Num a) => a -> [a] -> [[a]]
change 0 _ = [[]]
change n coins = [coin : result | coin <- coins, coin <= n, result <- change (n - coin) coins]