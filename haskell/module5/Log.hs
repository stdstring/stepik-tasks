import Control.Applicative
import Control.Monad

data Log a = Log [String] a

toLogger :: (a -> b) -> String -> (a -> Log b)
toLogger f msg x = Log [msg] $ f x

execLoggers :: a -> (a -> Log b) -> (b -> Log c) -> Log c
execLoggers x f g = Log [msg1, msg2] cValue where
    Log [msg1] bValue = f x
    Log [msg2] cValue = g bValue

returnLog :: a -> Log a
returnLog = Log []

bindLog :: Log a -> (a -> Log b) -> Log b
bindLog (Log sourceMessages x) logFun = let (Log destMessages result) = logFun x in Log (sourceMessages ++ destMessages) result

instance Functor Log where
    fmap = liftM

instance Applicative Log where
    pure = return
    (<*>) = ap

instance Monad Log where
    return = returnLog
    (>>=) = bindLog

execLoggersList :: a -> [a -> Log a] -> Log a
execLoggersList = foldl (>>=) . return