import hmac
import hashlib


def generate_hotp(secret_inner, message):

    hmac_k_new = hmac.digest(secret_inner, message, hashlib.sha1)
    s = hmac_k_new
    i = s[19] & 0xf
    b31_inner = int(str((s[i] & 0x7f) << 24) + str((s[i+1] & 0xff) << 16) + str((s[i+2] & 0xff) << 8) + str((s[i+3] & 0xff)))
    return str(b31_inner % 10**6).zfill(6)


if __name__ == '__main__':

    secret = bytes.fromhex('7a 36 ad a9 90 22 7c cc 18 34 8d 91 bc 6e d9 f0 b4 86 ea c6')
    counter = 0
    while True:
        b31 = generate_hotp(secret, bytes([counter]))
        print(b31)
        counter += 1
        user_input = input("Nächster Key? | y / n : ")
        if user_input == 'y':
            continue
        elif user_input == 'n':
            break

