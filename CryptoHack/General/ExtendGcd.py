def extend_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extend_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

print(extend_gcd(26513, 32321))