# -*- coding: iso-8859-1 -*-
import random


def read_txt():
    results = []
    with open('german-4.txt', 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            results.append(line.strip('\n'))
    return results


word_list = read_txt()
all_words_list = []
pin_list = []
found_pins = []

column_1 = ['s', 'e', 'h', 'g', 'p', 'i', 'u', 'i', 'h', 'k']
column_2 = ['r', 'i', 'e', 'e', 'ö', 'f', 'n', 'm', 's', 'z']
column_3 = ['c', 'a', 'g', 'q', 'ö', 't', 'ü', 'f', 'a', 'j']
column_4 = ['j', 'x', 'f', 'e', 'u', 'm', 'o', 'a', 'ö', 'a']


def calculate_pin(array_1, array_2, array_3, array_4):
    pin = ''
    own_word = ''
    for i in range(len(array_1)):
        for x in range(len(array_2)):
            for y in range(len(array_3)):
                for z in range(len(array_4)):
                    own_word += (array_1[i] + array_2[x] + array_3[y] + array_4[z])
                    pin += str(i) + str(x) + str(y) + str(z)
                    pin_list.append(pin)
                    all_words_list.append(own_word)
                    own_word = ''
                    pin = ''


def compare(array_1, array_2):
    x = 0
    for i in range(len(array_1)):
        for j in range(len(array_2)):
            if array_1[i] == array_2[j]:
                print(array_1[i] + ' match found line: ' + str(i) + ' PIN should be: ' + pin_list[j])
                found_pins.append(pin_list[j])
                x += 1
    return x


calculate_pin(column_1, column_2, column_3, column_4)

print('Es wurden: ' + str(compare(word_list, all_words_list)) + ' Übereinstimmungen gefunden.')


def guess_pin(pin, array_1):

    choice = random.choice(array_1)
    if choice == pin:
        return True
    else:
        array_1.remove(choice)


counter_wins, counter_lose = 0, 0
iterations = 100000
rounds_list = []
win_list = []
avg_number = 0

for a in range(iterations):
    counter_round = 0
    win_current = 0
    new_array = found_pins.copy()
    for b in range(3):

        if guess_pin('4112', new_array):
            counter_wins += 1
            win_list.append(1)
            win_current += 1
            counter_round += 1
            break
        else:
            counter_lose += 1
            counter_round += 1


    rounds_list.append(counter_round)
    if win_current == 0:
        win_list.append(0)

for p in range(len(rounds_list)):
    if win_list[p] == 1:
        avg_number += rounds_list[p]


print('Loses: ' + str(counter_lose))
print('Wins: ' + str(counter_wins))

print('Wahrscheinlichkeitsversuch: ' + str(counter_wins) + ':' + str(iterations) + ' = ' + str(counter_wins / iterations))

print('Die Wahrscheinlichkeit, dass ein Angreifer den PIN richtig errät liegt nach 3 Versuchen bei ca. ' +
      str(counter_wins / iterations * 100) + '%')

print(avg_number)
avg_number = avg_number/counter_wins
print('Anzahl der im Avg. gebrauchten Versuche, bei den Fällen, wo ein PIN erraten wurden : '+ str(avg_number))
