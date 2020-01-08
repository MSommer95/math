from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


if __name__ == '__main__':
    des_list = [
        '048ccd1fb6067ee0e304dc2025b96f4b',
        '296b66f3e332ab4c27501ca175c3b34d',
        '048ccd1fb6067ee0d4ca5da7e899def6',
        'bad5ede188bd1df1db8b06031867621a',
        '048ccd1fb6067ee0d6bd98bdb9a1a9b8a3f09b75107ca0da',
        'f316e31f45811c72c4e04380eac44e13',
        '47e046fb250a0b95cade3eff4ebda29c93157b2fc01c2430',
        '296b66f3e332ab4c27501ca175c3b34d',
    ]

    key = bytearray.fromhex('0ba950d08830c8079bded71b852934453db8f4ffff1f5842')
    algorithm = algorithms.TripleDES(key)
    cipher = Cipher(algorithm, mode=modes.CBC(bytearray.fromhex('821fd38b9a7c0247')), backend=default_backend())

    for string in des_list:
        decryptor = cipher.decryptor()
        print(decryptor.update(bytearray.fromhex(string)))
