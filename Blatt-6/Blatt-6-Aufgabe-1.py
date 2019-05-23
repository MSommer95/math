import textwrap
import operator


def encrypt_vigenere_chiffre(input_key, input_text):
    cipher = ''
    i = 0
    while i < len(input_text):
        for k in range(len(input_key)):
            key_index = ord(input_key[k]) - 97
            text_index = ord(input_text[i]) - 97
            cipher = cipher + chr((text_index + key_index) % 26 + 97)
            i = i + 1

            if i >= len(input_text):
                break
    return cipher


def decrypt_vigenere_chiffre(input_text, input_key):
    clear = ''
    i = 0
    while i < len(input_text):
        for k in range(len(input_key)):
            key_index = ord(input_key[k]) - 97
            text_index = ord(input_text[i]) - 97
            clear = clear + chr((text_index - key_index) % 26 + 97)
            i = i + 1

            if i >= len(input_text):
                break
    return clear


def analyze_cipher(input_text, split):
    key = ''
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

    for i in range(len(sorted_parts)):

        value_e = ord('e')-97

        for index in range(len(sorted_parts[i])):
            letter_list[sorted_parts[i][index]] += 1

        #for letter in letter_list:
        #    print(letter, (letter_list[letter] / len(sorted_parts[8])) * 100)

        max_value = max(letter_list.items(), key=operator.itemgetter(1))[0]

        max_value = ord(max_value)-97

        key = key + chr((max_value - value_e) % 26 + 97)

        for i in range(26):
            letter_list[chr(i + 97)] = 0

    return key


def kappa_test(input_text, split):

    sorted_parts = []
    durch_sum_med = 0

    for fill in range(split):
        sorted_parts.append('')
    parts = textwrap.wrap(input_text, split)
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
    if 0.064 < durch_sum_med < 0.072:
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


def friedman(koinzi, input_text):
    k = (0.0295 * len(input_text)) / (((len(input_text) - 1) * koinzi) - (0.0385 * len(input_text)) + 0.068)
    print('Friedmann: ' + str(k))


if __name__ == '__main__':
    cipher = ''
    krypto_text = ''
    whitelist = ''
    best_guess = 0

    f = open('geheimtext.txt', 'r')

    for line in f:
        krypto_text = krypto_text + (line.strip().replace(' ', ''))
    f.close()

    for i in range(26):
        whitelist = whitelist + chr(i+97)

    krypto_text = ''.join(filter(whitelist.__contains__, krypto_text))
    print(krypto_text)
    print(len(krypto_text))

    for x in range(1, 30):
        best_guess = kappa_test(krypto_text, x)
        if best_guess > 0:
            break
    print(best_guess)
    friedman(koinzidenzindex(krypto_text), krypto_text)

    key = analyze_cipher(krypto_text, best_guess)
    print('Der Schlüssel: ' + key)

    decrypted_text = decrypt_vigenere_chiffre(krypto_text, key)

    print(decrypted_text)

    test_cipher = encrypt_vigenere_chiffre('cardinal', decrypted_text)
