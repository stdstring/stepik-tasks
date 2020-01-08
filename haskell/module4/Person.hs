data Person = Person { firstName :: String, lastName :: String, age :: Int }

updateLastName :: Person -> Person -> Person
updateLastName p1 p2 = p2 {lastName = (lastName p1)}

abbrFirstName :: Person -> Person
abbrFirstName p@(Person {firstName=fName}) | length fName < 2 = p
                                           | otherwise = p {firstName = ([head fName, '.'])}