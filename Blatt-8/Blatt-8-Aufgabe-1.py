
a = 5
b = 96


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
