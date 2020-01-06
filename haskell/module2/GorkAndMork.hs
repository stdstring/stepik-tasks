class KnownToGork a where
    stomp :: a -> a
    doesEnrageGork :: a -> Bool

class KnownToMork a where
    stab :: a -> a
    doesEnrageMork :: a -> Bool

class (KnownToGork a, KnownToMork a) => KnownToGorkAndMork a where
    stompOrStab :: a -> a
    stompOrStab value | (doesEnrageGork value) && (doesEnrageMork value) = (stomp.stab) value
    stompOrStab value | doesEnrageGork value = stab value
    stompOrStab value | doesEnrageMork value = stomp value
    stompOrStab value = value