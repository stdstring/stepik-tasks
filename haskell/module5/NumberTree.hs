import Control.Monad.State

data Tree a = Leaf a | Fork (Tree a) a (Tree a)

processTree :: Tree () -> State (Integer, Tree Integer) ()
processTree sourceTree = do
    (currentNumber, _) <- get
    case sourceTree of
        Leaf () -> put (currentNumber + 1, Leaf currentNumber)
        Fork left () right -> do
            put $ (currentNumber, Leaf 0)
            processTree left
            (leftNumber, leftResult) <- get
            put $ (leftNumber + 1, Leaf 0)
            processTree right
            (rightNumber, rightResult) <- get
            put (rightNumber, Fork leftResult leftNumber rightResult)

numberTree :: Tree () -> Tree Integer
numberTree tree = let (_, resultTree) = execState (processTree tree) (1, Leaf 0) in resultTree