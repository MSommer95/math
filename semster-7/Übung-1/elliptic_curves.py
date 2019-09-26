
def check_for_equal(P, a, b, p):

    compare_y = pow(P[1], 2) % p
    compare_x = (pow(P[0], 3) + a*P[0] + b) % p

    if compare_y == compare_x:
        return True
    else:
        return False


def check_for_not_null(a, b):

    check_val = 4 * pow(a, 3) + 27 * pow(b, 2)

    if check_val != 0:
        return check_val
    else:
        return False


def point_addition(P, Q, p):

    number1 = (P[1] - Q[1]) % p
    number2 = (mulinv((P[0] - Q[0]) % p, p)) % p

    s = (number1 * number2) % p

    xC = (s**2 - P[0] - Q[0]) % p
    yC = (-P[1] - s * (xC - P[0])) % p

    newP = (xC, yC)
    return newP


def point_multiply(P, a, p):

    number1 = (3 * pow(P[0], 2) + a) % p
    number2 = mulinv((2 * P[1]) % p, p) % p

    s = (number1 * number2) % p

    xC = (pow(s, 2) - 2 * P[0]) % p
    yC = (-P[1] - s * (xC - P[0])) % p

    newP = (xC, yC)
    return newP


def bits(n):

    bits = []

    for i in range(3, len(bin(n))):
        bits.append(bin(n)[i])
    return bits


def double_and_add(n, P, a, p):

    N = P

    for i in range(len(bits(n))):

        N = point_multiply(N, a, p)

        if bits(n)[i] == '1':
            N = point_addition(N, P, p)

    return N


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


if __name__ == '__main__':
    # Aufgabe 1

    a = 2
    b = 2
    p = 17

    #a)
    print('Zeigen Sie, dass die Bedingung 4a3 + 27b2 ̸= 0 erfüllt ist')
    print(check_for_not_null(a, b))

    #b)
    print('Zeigen Sie, dass der Punkt (9, 1) die Kurvengleichung erfüllt.')
    print(check_for_equal((9, 1), a, b, p))

    #c)
    print('Berechnen Sie die Verdoppelung des Punktes (9, 1).')
    print(point_multiply((9, 1), a, p))

    #d)
    print('Berechnen Sie die Addition der Punkte (7, 9) und (0, 2).')
    P = (7, 9)
    Q = (0, 2)
    print(point_addition(P, Q, p))
    print(check_for_equal((11, 4), a, b, p))



