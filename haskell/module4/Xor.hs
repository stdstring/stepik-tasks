import Data.Monoid

newtype Xor = Xor { getXor :: Bool } deriving (Eq,Show)

instance Semigroup Xor where
    (<>) (Xor x) (Xor y) = Xor (x /= y)

instance Monoid Xor where
    mempty = Xor False
