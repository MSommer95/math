import time


def squareAndMulti(x, y):
    value = x
    exp = bin(y)
    for i in range(3, len(exp)):
        value = value * value
        if exp[i:i + 1] == '1':
            value = value * x
    return value


start_time = time.time()
print(3**181)
print((time.time()-start_time))

start_time = time.time()
print(squareAndMulti(3, 181))
print((time.time()-start_time))
