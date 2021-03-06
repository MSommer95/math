
a = 5
b = 96

werteR = []
werteQ = []
werteA = []
ergebnisse = []


def ggt(a, b):
    x = b
    y = a % b

    multipli = int(a / b)

    werteR.append(multipli)
    werteQ.append(y)
    werteA.append(x)
    if y == 0:
        return x

    return ggt(x, y)


print('Der ggt(' + str(a) + ',' + str(b) + ') ist: ' + str(ggt(a, b)))
print(werteQ)
print(werteR)


def erwEuklid(werteQ, werteR, i, x, y):

    yi = werteR[i]
    ergebnis = x - yi * y
    ergebnisse.append(ergebnis)

    if i == 0:
        return True

    return erwEuklid(werteQ, werteR, i-1, y, ergebnis)


erwEuklid(werteQ, werteR, len(werteR)-2, 0, 1)

print(ergebnisse)

print('Der ggt(' + str(a) + ',' + str(b) + ') ist: ' + str(ggt(a, b)) + '=' + str(ergebnisse[len(ergebnisse)-2]) + '*'
      + str(a) + '+' + str(ergebnisse[len(ergebnisse)-1]) + '*' + str(b))

ergebnis = ergebnisse[len(ergebnisse)-2]

if ergebnis < 0:
    ergebnis = ergebnis + b

zwischenErgebnis = (a * ergebnis) % b

if (a * ergebnis % b) != 1:
    ergebnis = ergebnisse[len(ergebnisse) - 1]

if ergebnis < 0:
    ergebnis = (ergebnisse[len(ergebnisse)-2] + (a * b)) % a


print('Inverse: ' + str(a) + '^-1 = ' + str(ergebnis) + ' mod ' + str(b))