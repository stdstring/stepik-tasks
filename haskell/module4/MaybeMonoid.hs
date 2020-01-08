import Data.Monoid

newtype Maybe' a = Maybe' { getMaybe :: Maybe a } deriving (Eq,Show)

instance Semigroup a => Semigroup (Maybe' a) where
    (Maybe' Nothing) <> _ = Maybe' Nothing
    _ <> (Maybe' Nothing) = Maybe' Nothing
    (Maybe' l) <> (Maybe' r) = Maybe' (l `mappend` r)

instance Monoid a => Monoid (Maybe' a) where
    mempty = Maybe' (Just mempty)