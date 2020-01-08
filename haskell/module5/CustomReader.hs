import Control.Applicative
import Control.Monad

data Reader r a = Reader { runReader :: (r -> a) }

instance Functor (Reader r) where
    fmap = liftM

instance Applicative (Reader r) where
    pure = return
    (<*>) = ap

instance Monad (Reader r) where
    return x = Reader $ \_ -> x
    m >>= k  = Reader $ \r -> runReader (k (runReader m r)) r

local' :: (r -> r') -> Reader r' a -> Reader r a
local' f m = Reader $ \e -> runReader m (f e)