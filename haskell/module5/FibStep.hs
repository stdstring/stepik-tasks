import Control.Monad.State

fibStep :: State (Integer, Integer) ()
fibStep = modify $ \(prev, current) -> (current, current + prev)

execStateN :: Int -> State s a -> s -> s
execStateN n m = execState (replicateM_ n m)