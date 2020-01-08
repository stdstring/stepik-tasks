data Bit = Zero | One
data Sign = Minus | Plus
data Z = Z Sign [Bit]

convertToInteger (Z Minus bits) = -1 * (convertToInteger (Z Plus bits))
convertToInteger (Z Plus bits) = convertToIntegerImpl bits
    where
        convertBitToInteger Zero = 0
        convertBitToInteger One = 1
        convertToIntegerImpl = foldr (\bit result -> result * 2 + (convertBitToInteger bit)) 0

convertToZ 0 = Z Plus []
convertToZ number | number > 0 = Z Plus $ convertToZImpl number
                  | number < 0 = Z Minus $ convertToZImpl (-number)
    where
        convertIntegerToBit 0 = Zero
        convertIntegerToBit 1 = One
        convertToZImpl 0 = []
        convertToZImpl number = (convertIntegerToBit $ number `mod` 2) : convertToZImpl (number `div` 2)

add :: Z -> Z -> Z
add a b = convertToZ ((convertToInteger a) + (convertToInteger b))

mul :: Z -> Z -> Z
mul a b = convertToZ ((convertToInteger a) * (convertToInteger b))
