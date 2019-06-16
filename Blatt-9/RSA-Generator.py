
p = 7
q = 11

n = p * q

phiN = (p-1) * (q-1)


def ggT(x, y):
   z = x % y
   if z == 0:
      return y
   return ggT(y, z)


def erwEuklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = erwEuklid(b % a, a)
        return (g, y - (b // a) * x, x)


def mulinv(a, b):
    g, x, _ = erwEuklid(a, b)
    if g == 1:
        return x % b


print(ggT(13, phiN))
print(erwEuklid(13, phiN))

print(mulinv(13, phiN))

e = 13
d = mulinv(e, phiN)

m1 = 45 % n
m2 = 80 % n

print('M1 ' + str(m1))
print('M2 ' + str(m2))

c1 = (m1**e) % n
c2 = (m2**e) % n

print('C1 ' + str(c1))
print('C2 ' + str(c2))

d1 = (c1**d) % n
d2 = (c2**d) % n

print('D1 ' + str(d1))
print('D2 ' + str(d2))
