import Data.List.Split (splitOn)
import qualified Data.Set as Set

data Error = ParsingError | IncompleteDataError | IncorrectDataError String

data Person = Person { firstName :: String, lastName :: String, age :: Int }

parsePerson :: String -> Either Error Person
parsePerson inputData = parsePersonData (splitOn "\n" inputData) Person{} Set.empty where
    stringToAge value =
        case reads value :: [(Int, String)] of
            [(age, "")] -> Just age
            _ -> Nothing
    parsePersonData [] person parsedFields =
        case parsedFields == (Set.fromList ["firstName", "lastName", "age"]) of
            True -> Right person
            False -> Left IncompleteDataError
    parsePersonData (item : items) person parsedFields =
        case splitOn " = " item of
            ["firstName", value] -> parsePersonData items (person{firstName = value}) (Set.insert "firstName" parsedFields)
            ["lastName", value] -> parsePersonData items (person{lastName = value}) (Set.insert "lastName" parsedFields)
            ["age", value] ->
                case stringToAge value of
                    Just ageValue -> parsePersonData items (person{age = ageValue}) (Set.insert "age" parsedFields)
                    Nothing -> Left $ IncorrectDataError value
            [_, _] -> parsePersonData items person parsedFields
            _ -> Left ParsingError