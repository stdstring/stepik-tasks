class (Eq a, Enum a, Bounded a) => SafeEnum a where
  ssucc :: a -> a
  ssucc value | value == maxBound = minBound
  ssucc value | otherwise = succ value

  spred :: a -> a
  spred value | value == minBound = maxBound
  spred value | otherwise = pred value

instance SafeEnum Bool