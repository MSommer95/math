import random
import string
import hashlib, binascii


def password_generator(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


if __name__ == '__main__':
    h = hashlib.new('sha1')
    random_password = password_generator(12)

    figur = input('Wähle eine Figur (Stein, Schere, Papier): ')
    print("Your random password is: ", random_password)

    h.update(random_password.encode())
    print(h.hexdigest())

    my_hash = hashlib.pbkdf2_hmac('sha1', random_password.encode(), figur.encode(), 1)
    print('Ihr Hashwert für die Figur ' + figur + ': ' + str(binascii.hexlify(my_hash)))

    hash_controll = input('Geben sie den Hashwert ihres Partners an: ')

    partner_hash = hashlib.pbkdf2_hmac('sha1', input('Gebe das Passwort des Partners an: ').encode(),
                                       input('Gebe die Figur des Partners an: ').encode(), 1)
    print('Ihr Hashwert für die Figur ' + figur + ': ' + str(binascii.hexlify(partner_hash)))

    partner_hash = str(binascii.hexlify(partner_hash))

    if 'b\'' + hash_controll + '\'' == partner_hash:
        print('Ihr Partner spielt fair')
