data Entry k1 k2 v = Entry (k1, k2) v  deriving Show
data Map k1 k2 v = Map [Entry k1 k2 v]  deriving Show

instance Functor (Entry k1 k2) where
    fmap g (Entry key v) = Entry key (g v)

instance Functor (Map k1 k2) where
    fmap g (Map entries) = Map $ fmap (fmap g) entries