import Control.Monad.Writer.Lazy

evalWriter :: Writer w a -> a
evalWriter = fst . runWriter