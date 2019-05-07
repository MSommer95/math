
import textwrap
from collections import Counter

def encrypt_vigenere_chiffre(input_key, input_text, i):
    cipher = ''
    while i < len(input_text):
        for k in range(len(input_key)):
            key_index = ord(input_key[k]) - 97
            text_index = ord(input_text[i]) - 97
            cipher = cipher + chr((text_index + key_index) % 26 + 97)
            i = i + 1

            if i >= len(input_text):
                break
    return cipher


def analyze_cipher(input_text, split):

    sorted_parts = []
    letter_list = {}

    for i in range(26):
        letter_list[chr(i + 97)] = 0

    for fill in range(split):
        sorted_parts.append('')
    parts = textwrap.wrap(input_text, split)

    for i in range(len(parts)):
        for j in range(split):
            if j < len(parts[i]):
                sorted_parts[j] = sorted_parts[j] + parts[i][j]
            else:
                break

    print(sorted_parts)

    for index in range(len(sorted_parts[8])):
        letter_list[sorted_parts[8][index]] += 1

    for letter in letter_list:
        print(letter, (letter_list[letter] / len(sorted_parts[8]))*100)

    print(letter_list)

def decrypt_vigenere_chiffre(input_text, key):
    clear = ''
    i = 0
    while i < len(input_text):
        for k in range(len(key)):
            key_index = ord(key[k]) - 97
            text_index = ord(input_text[i]) - 97
            clear = clear + chr((text_index - key_index) % 26 + 97)
            i = i + 1

            if i >= len(input_text):
                break
    return clear


def kappa_test(input_text, split, best_guess):
    sorted_parts = []
    durch_sum_med = 0

    for fill in range(split):
        sorted_parts.append('')
    parts = textwrap.wrap(input_text, split)
    #print(parts)
    for i in range(len(parts)):
        for j in range(split):
            if j < len(parts[i]):
                sorted_parts[j] = sorted_parts[j] + parts[i][j]
            else:
                break
    for length in range(len(sorted_parts)):
        #print('Teil-Alphabet Nummer ' + str(length)+ ' : ' + sorted_parts[length])
        durch_sum_med = durch_sum_med + koinzidenzindex(sorted_parts[length])

    durch_sum_med = durch_sum_med / len(sorted_parts)
    print('Koinzidenzindex für Split: ' + str(split) + ' :' + str(durch_sum_med))
    if 0.060 < durch_sum_med < 0.070:
        print('Found guess: ' + str(durch_sum_med))
        best_guess = split
        return best_guess
    else:
        return 0


def koinzidenzindex(teil_alphabet):

    letter_list = {}
    sum_med = 0

    for i in range(26):
            letter_list[chr(i + 97)] = 0

    for index in range(len(teil_alphabet)):
        letter_list[teil_alphabet[index]] += 1

    for sum in letter_list:
        sum_med = sum_med + (letter_list[sum] * (letter_list[sum] - 1))

    sum_med = sum_med / (len(teil_alphabet) * (len(teil_alphabet) - 1))

    return sum_med


def friedman(koinzi, krypto_text):
    k = (0.0295 * len(krypto_text)) / (((len(krypto_text) - 1) * koinzi) - (0.0385 * len(krypto_text)) + 0.068)
    print(k)


if __name__ == '__main__':
    cipher = ''
    krypto_text = ''
    key = ''
    whitelist = ''
    best_guess = 0
    i = 0
    l = 1
    f = open('geheimtext.txt', 'r')

    for line in f:
        krypto_text = krypto_text + (line.strip().replace(' ', ''))
    f.close()

    for i in range(26):
        whitelist = whitelist + chr(i+97)

    krypto_text = ''.join(filter(whitelist.__contains__, krypto_text))
    print(krypto_text)
    print(len(krypto_text))

    test_crypto = 'XOQWIJGBIXRVKT'.lower()
    test_key = 'igloskbso'
    print(decrypt_vigenere_chiffre(krypto_text, test_key))

    for x in range(1, 30):
        best_guess = kappa_test(krypto_text, x, best_guess)
        if best_guess > 0:
            break
    print(best_guess)
    friedman(koinzidenzindex(krypto_text), krypto_text)

    analyze_cipher(krypto_text, best_guess)



    #
    #input_key = list(input("Geben sie einen Key ein: ").lower())
    #input_text = list(input("Geben sie einen Satz ein: ").lower())
    #
    #print(encrypt_vigenere_chiffre(input_key, input_text, i))

