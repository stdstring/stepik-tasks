import Prelude hiding (lookup)

class MapLike m where
    empty :: m k v
    lookup :: Ord k => k -> m k v -> Maybe v
    insert :: Ord k => k -> v -> m k v -> m k v
    delete :: Ord k => k -> m k v -> m k v
    fromList :: Ord k => [(k,v)] -> m k v

newtype ArrowMap k v = ArrowMap { getArrowMap :: k -> Maybe v }

instance MapLike (ArrowMap) where
    empty = ArrowMap (\k -> Nothing)
    lookup key entry = (getArrowMap entry) key
    insert key value entry = ArrowMap (\k -> case k == key of {True -> Just value; False -> (getArrowMap entry) k})
    delete key entry = ArrowMap (\k -> case k == key of {True -> Nothing; False -> (getArrowMap entry) k})
    fromList = foldr (\(key, value) entry -> insert key value entry) empty