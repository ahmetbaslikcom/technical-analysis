def yukariKes(a, b):
    oncekiKisa = a[len(a) - 3]
    kisa = a[len(a) - 2]
    simdikisa = a[len(a) - 1]

    oncekiUzun = b[len(b) - 3]
    uzun = b[len(b) - 2]
    simdiuzun = b[len(b) - 1]
    if oncekiKisa < oncekiUzun and kisa > uzun and simdikisa > simdiuzun:
        return True
    else:
        return False

      
def asagiKes(a, b):
    oncekiKisa = a[len(a) - 3]
    kisa = a[len(a) - 2]
    simdikisa = a[len(a) - 1]
    oncekiUzun = b[len(b) - 3]
    uzun = b[len(b) - 2]
    simdiuzun = b[len(b) - 1]
    if oncekiKisa > oncekiUzun and kisa < uzun and simdikisa < simdiuzun:
        return True
    else:
        return False
