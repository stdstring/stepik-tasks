data Result = Fail | Success

data SomeData

doSomeWork :: SomeData -> (Result,Int)
doSomeWork _ = undefined

processData :: SomeData -> String
processData inputData =
    case doSomeWork inputData of
        (Success, 0) -> "Success"
        (Fail, errorCode) -> "Fail: " ++ (show errorCode)

data Result' = SuccessResult | FailResult Int

instance Show Result' where
    show (SuccessResult) = "Success"
    show (FailResult errorCode) = "Fail: " ++ (show errorCode)

doSomeWork' :: SomeData -> Result'
doSomeWork' inputData =
    case doSomeWork inputData of
        (Success, 0) -> SuccessResult
        (Fail, errorCode) -> FailResult errorCode