import qualified Data.List as L
import System.Directory(getDirectoryContents, removeFile)

main' :: IO ()
main' = do
    putStr "Substring: "
    subStr <- getLine
    if subStr == "" then putStrLn "Canceled" else do
        filenames <- getDirectoryContents "."
        mapM_ (\fname -> do {putStrLn $ "Removing file: " ++ fname; removeFile fname}) $ filter (\fname -> L.isInfixOf subStr fname) filenames