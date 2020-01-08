import Control.Monad.State
import Control.Monad.Writer.Lazy

writerToState :: Monoid w => Writer w a -> State w a
writerToState m = state $ \s -> let (a, w) = runWriter m in (a, s `mappend` w)