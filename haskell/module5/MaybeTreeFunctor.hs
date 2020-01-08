import Data.Functor
import Data.Maybe

data Tree a = Leaf (Maybe a) | Branch (Tree a) (Maybe a) (Tree a) deriving Show

instance Functor Tree where
    fmap f (Leaf x) = Leaf (f <$> x)
    fmap f (Branch l x r) = Branch (f <$> l) (f <$> x) (f <$> r)