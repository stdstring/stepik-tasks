import Control.Monad.Reader

type User = String
type Password = String
type UsersTable = [(User, Password)]

usersWithBadPasswords :: Reader UsersTable [User]
usersWithBadPasswords = asks (map fst . filter (\entry -> (snd entry) == "123456"))