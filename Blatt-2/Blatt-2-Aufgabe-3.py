import os
import hashlib
import itertools
import time
from datetime import datetime
from multiprocessing import Process, current_process


def create_ingredients():
    password_ingredients = ''

    for i in range(ord('a'), ord('z')+1):
        password_ingredients += chr(i)

    for j in range(ord('A'), ord('Z')+1):
        password_ingredients += chr(j)

    for x in range(10):
        password_ingredients += str(x)

    return password_ingredients


def create_password(input_value, ingredients, password_length, combinations_number, current_hash, start_time, user_input, process_count):
    print(f"Process ID: {current_process().name}")
    for counter, item in enumerate(itertools.islice(itertools.product(ingredients, repeat=password_length),
                                                    int(combinations_number * input_value/process_count),
                                                    int(combinations_number * (input_value+1)/process_count))):
        if hashlib.sha1(''.join(item).encode()).hexdigest() == current_hash:
            elapsed_time = time.time() - start_time
            print('Password for ' + user_input + ': ' + ''.join(item))
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys pro Sekunde: ' + str(counter / elapsed_time))
            print('Getestete Keys: ' + str(counter))
            break


def hash_generated_passwords_joe(input_array):

    for counter, item in enumerate(input_array):
        if hashlib.sha1(item.encode()).hexdigest() == current_hash:
            elapsed_time = time.time() - start_time
            print('Password for ' + user_input + ': ' + ''.join(item))
            print('Gebrauchte Zeit zum Knacken: ' + str(elapsed_time))
            print('Getestete Keys: ' + str(counter))


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



    if user_input != 'joe':
        password_length = int(input('Wie lang soll das Passwort sein? '))
        ingredients = create_ingredients()
        print('Ingredients: ' + ingredients)
        combinations_number = 62 ** password_length
        print('Kominationsmöglichkeiten: ' + str(combinations_number))
        dt_object = datetime.fromtimestamp(time.time())
        print(dt_object)
        current_hash = hashes[password_length-1]
        start_time = time.time()
        process_count = 8
        processes = []
        for input_value in range(process_count):
            process = Process(target=create_password, args=(input_value, ingredients, password_length,
                                                            combinations_number, current_hash, start_time,
                                                            user_input, process_count))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        elapsed_time = time.time() - start_time
        print('Gebrauchte Zeit für einen kompletten Durchlauf: ' + str(elapsed_time))

    if user_input == 'joe':
        combinations_number = 100
        print('Passwörter: ' + str(combinations_number))
        dt_object = datetime.fromtimestamp(time.time())
        print(dt_object)
        current_hash = hashes[0]
        start_time = time.time()
        hash_generated_passwords_joe(passwords)
