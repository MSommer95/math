
a = 34512423561108014234
b = 115792089210356248762697446949407573530086143415290314195533631308867097853951


def erwEuklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = erwEuklid(b % a, a)
        return (g, y - (b // a) * x, x)


print(erwEuklid(a, b))


def mulinv(a, b):
    g, x, _ = erwEuklid(a, b)
    if g == 1:
        return x % b


print(mulinv(a, b))

print((mulinv(a, b) * a) % b)
