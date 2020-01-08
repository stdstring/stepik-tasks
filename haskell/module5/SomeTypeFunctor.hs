-- data SomeType a = ...

-- instance Monad SomeType where

instance Functor SomeType where
    fmap f x = x >>= (return . f)