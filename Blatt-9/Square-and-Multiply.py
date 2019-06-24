import time


def squareAndMulti(x, y):
    value = x
    exp = bin(y)

    for i in range(3, len(exp)):
        value = value * value
        if exp[i:i + 1] == '1':
            value = value * x
    return value


def modexp_mul(a, b, n):
    r = 1
    for i in range(b):
        r = r * a % n
    return r


def modexp_rl(a, b, n):
    r = 1
    while 1:
        if b % 2 == 1:
            r = r * a % n
        b /= 2
        if b == 0:
            break
        a = a * a % n

    return r


def modexp_lr(a, b, n):
    r = 1
    for bit in reversed(_bits_of_n(b)):
        r = r * r % n
        if bit == 1:
            r = r * a % n
    return r


def _bits_of_n(n):
    """ Return the list of the bits in the binary
        representation of n, from LSB to MSB
    """
    bits = []

    while n:
        bits.append(n % 2)
        n /= 2

    return bits

start_time = time.time()
print('simple: ' + str((1234567**1234567)% 1234))
print((time.time()-start_time))

start_time = time.time()
print('pow: ' + str(pow(1234567, 1234567, 1234)))
print((time.time()-start_time))

start_time = time.time()
print('SaM: ' + str(squareAndMulti(1234567, 1234567) % 1234))
print((time.time()-start_time))

start_time = time.time()
print('modexp_mul: ' + str(modexp_mul(1234567, 1234567, 1234)))
print((time.time()-start_time))

start_time = time.time()
print('modexp_rl: ' + str(modexp_rl(1234567, 1234567, 1234)))
print((time.time()-start_time))

start_time = time.time()
print('modexp_lr: ' + str(modexp_lr(1234567, 1234567, 1234)))
print((time.time()-start_time))

#start_time = time.time()
#print((2345149 ** 36503778) % 323453257)
#print((time.time()-start_time))
