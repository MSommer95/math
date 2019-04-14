import hashlib
import time
from datetime import datetime
from multiprocessing import Process, current_process


def create_password(input_value, start_value, end_value, current_hash, process_count, start_time):
    print(f"Process ID: {current_process().name}")

    for index in range(start_value, end_value):
        value_range = 2**index
        print(index)
        for counter, number in enumerate(range(int(value_range * (input_value/(process_count+1))), int(value_range * ((input_value + 1)/(process_count+1))))):
            new_hash = hashlib.sha256((str(number) + current_hash + 'Sommer').encode()).hexdigest()
            if int(new_hash, 16) < int(current_hash, 16) / 2:
                print('Hashwert korrekt für Zahl: ' + str(number) + f" Process ID: {current_process().name}")
                print(new_hash)
                print((time.time()-start_time))
                a = open('Aufgaben-Antworten.txt', 'a')
                a.write(str(number))
            if counter >= 100000000:
                break


if __name__ == '__main__':
    current_hash = '000000000e6cc4699001de147eb80dfabf597758119ab203aadaabf5598523c4'
    length1 = '0000000000000000000d1313bd1345db31548560c97cbcb9acc1724addd9f278'
    length1_value = 2**(len(length1)*4)
    length2 = 'd1313bd1345db31548560c97cbcb9acc1724addd9f278'
    length2_value = 2**(len(length2)*4)

    print(length1_value)
    print(length2_value)

    print((length2_value/length1_value)*100)

    processes = []
    process_count = 6
    start_value = 135
    end_value = 256
    dt_object = datetime.fromtimestamp(time.time())
    print(dt_object)
    start_time = time.time()

    for input_value in range(1, process_count+1):
        process = Process(target=create_password, args=(input_value, start_value, end_value, current_hash,
                                                        process_count, start_time))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    elapsed_time = time.time() - start_time
    print('Gebrauchte Zeit für einen kompletten Durchlauf: ' + str(elapsed_time))