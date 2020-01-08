data List a = Nil | Cons a (List a)

fromList :: List a -> [a]
fromList Nil = []
fromList (Cons x source) = x : (fromList source)

toList :: [a] -> List a
toList = foldr Cons Nil