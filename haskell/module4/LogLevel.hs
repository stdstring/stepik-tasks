data LogLevel = Error | Warning | Info

cmp :: LogLevel -> LogLevel -> Ordering
cmp Error Error = EQ
cmp Error Warning = GT
cmp Error Info = GT
cmp Warning Error = LT
cmp Warning Warning = EQ
cmp Warning Info = GT
cmp Info Error = LT
cmp Info Warning = LT
cmp Info Info = EQ