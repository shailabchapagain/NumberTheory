def modular(a,b):
        while a>=b:
            a=a-b
        return a


def gcd(a, b):
    while b:
        a, b = b, modular(a,b)
    return a
