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

    a = 0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300
    b = 0x1E589A8595423412134FAA2DBDEC95C8D8675E58
    p = 0xE95E4A5F737059DC60DFC7AD95B3D8139515620F
    P = (0xBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3, 0x1667CB477A1A8EC338F94741669C976316DA6321)

    d_1 = 197919899782636687082760
    d_2 = 509549134202698380559908

    R_1 = double_and_add(d_1, P, a, p)
    print(hex(R_1[0]))
    print(hex(R_1[1]))

    print('---------------------------------------------------')

    R_2 = double_and_add(d_2, P, a, p)
    print(hex(R_2[0]))
    print(hex(R_2[1]))

    print('---------------------------------------------------')

    Q = point_addition(R_1, R_2, p)
    Q_a = double_and_add((d_1 + d_2), P, a, p)

    print(Q)
    print(Q_a)

    print('---------------------------------------------------')




