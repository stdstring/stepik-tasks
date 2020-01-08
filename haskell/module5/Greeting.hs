main' :: IO ()
main' = do
    name <- retrieveName
    putStrLn $ "Hi, " ++ name ++ "!"

retrieveName :: IO String
retrieveName = do
    putStrLn "What is your name?"
    putStr "Name: "
    name <- getLine
    if (name == "") then retrieveName else return name