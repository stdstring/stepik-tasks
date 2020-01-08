data Nat = Zero | Suc Nat

fromNat :: Nat -> Integer
fromNat Zero = 0
fromNat (Suc n) = fromNat n + 1

toNat :: Integer -> Nat
toNat n = foldr (\_ natValue -> Suc natValue) Zero [1..n]

add :: Nat -> Nat -> Nat
add n1 n2 = toNat ((fromNat n1) + (fromNat n2))

mul :: Nat -> Nat -> Nat
mul n1 n2 = toNat ((fromNat n1) * (fromNat n2))

fac :: Nat -> Nat
fac n = toNat (foldl (*) 1 [1..fromNat n])