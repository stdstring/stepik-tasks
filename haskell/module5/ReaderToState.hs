import Control.Monad.Reader
import Control.Monad.State

readerToState :: Reader r a -> State r a
readerToState m = state $ \s -> let a = runReader m s in (a, s)