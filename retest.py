def retestUp(a, b):
    k3 = a[len(a) - 4]
    k2 = a[len(a) - 3]
    k1 = a[len(a) - 2]
    k0 = a[len(a) - 1]
    u3 = b[len(b) - 4]
    u2 = b[len(b) - 3]
    u1 = b[len(b) - 2]
    u0 = b[len(b) - 1]
    if k3 > k2 and k2 < k1 < k0 and k3 > u3 and k2 < u2 * 1.0008 and k1 > u1 * 1.0008 and k0 > u0:
        return True
    else:
        return False


def retestDown(a, b):
    k3 = a[len(a) - 4]
    k2 = a[len(a) - 3]
    k1 = a[len(a) - 2]
    k0 = a[len(a) - 1]
    u3 = b[len(b) - 4]
    u2 = b[len(b) - 3]
    u1 = b[len(b) - 2]
    u0 = b[len(b) - 1]
    if k3 < k2 and k2 > k1 > k0 and k3 < u3 and k2 > u2 * 0.9992 and k1 < u1 * 0.9992 and k0 < u0:
        return True
    else:
        return False
