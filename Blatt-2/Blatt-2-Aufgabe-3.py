from tensorflow import keras
import hashlib
import itertools
import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool


def create_ingredients():
    password_ingredients = ''

    for i in range(ord('a'), ord('z')+1):
        password_ingredients += chr(i)

    for j in range(ord('A'), ord('Z')+1):
        password_ingredients += chr(j)

    for x in range(10):
        password_ingredients += str(x)

    return password_ingredients


def create_password():
    global test_key_counter

    for item in itertools.product(ingredients, repeat=password_length):
        test_key_counter += 1
        if hashlib.sha1(''.join(item).encode()).hexdigest() == current_hash:
            elapsed_time = time.time() - start_time
            print('Password for ' + user_input + ': ' + ''.join(item))
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(test_key_counter / elapsed_time))
            print('Getestete Keys: ' + str(test_key_counter))
            break


def hash_generated_passwords(x):
    return


if __name__ == '__main__':
    #pool = ThreadPool()
    user_input = input('Nutzername: ')
    test_key_counter = 0
    combinations_number = 0
    hashes = []
    passwords = []
    current_hash = ''

    f = open('adobe-top100.txt', 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        passwords.append(columns[3])

    f.close()

    f = open('hashed_passwords', 'r')
    for line in f:
        line = line.strip()
        columns = line.split()
        hashes.append(columns[1])

    f.close()

    ingredients = create_ingredients()

    if user_input != 'joe':
        password_length = int(input('Wie lang soll das Passwort sein? '))
        combinations_number = 62 ** password_length
        print('Ingredients: ' + ingredients)
        print('Kominationsmöglichkeiten: ' + str(combinations_number))
        start_time = time.time()
        dt_object = datetime.fromtimestamp(time.time())
        print(dt_object)
        current_hash = hashes[password_length-1]
        create_password()

    if user_input == 'joe':
        range_iteration = range(len(passwords))
