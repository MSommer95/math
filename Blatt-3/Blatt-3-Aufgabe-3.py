import hashlib
import time
from datetime import datetime
from multiprocessing import Process, current_process


def create_password(input_value, combinations_number, current_hash, process_count, start_time):
    print(f"Process ID: {current_process().name}")
    for number in range(int(combinations_number * (input_value/process_count)), int(combinations_number * ((input_value + 1)/process_count))):
        new_hash = hashlib.sha256((str(number) + current_hash + 'Sommer').encode()).hexdigest()
        if int(new_hash, 16) < int(current_hash, 16) / 2:
            print('Hashwert korrekt für Zahl: ' + str(number) + f" Process ID: {current_process().name}")
            print(new_hash)
            print((time.time()-start_time))


if __name__ == '__main__':
    current_hash = '000000000e6cc4699001de147eb80dfabf597758119ab203aadaabf5598523c4'
    processes = []
    process_count = 7
    combinations_number = 2**102
    print('Kominationsmöglichkeiten: ' + str(combinations_number))
    dt_object = datetime.fromtimestamp(time.time())
    print(dt_object)
    start_time = time.time()

    for input_value in range(process_count):
        process = Process(target=create_password, args=(input_value, combinations_number, current_hash,
                                                        process_count, start_time))
        processes.append(process)
        process.start()

    for process in processes:
            process.join()

    elapsed_time = time.time() - start_time
    print('Gebrauchte Zeit für einen kompletten Durchlauf: ' + str(elapsed_time))
    print('Keyvergleiche pro Sekunde: ' + str(combinations_number / elapsed_time))