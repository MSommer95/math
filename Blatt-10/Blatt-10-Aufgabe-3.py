import time
from datetime import datetime
from multiprocessing import Process, current_process


def key_search(p, g, X, Y, input_value, process_count):
    for i in range(int(p * (input_value/process_count)), int(p/(input_value+1/process_count))):
        ergebnis = pow(g,i,p)
        if ergebnis == X:
            print('X: ' + str(i))
        if ergebnis == Y:
            print('Y: ' + str(i))


if __name__ == '__main__':
    p = 323453257
    g = 2345149
    X = 205125783
    Y = 71774435

    processes = []
    process_count = 32

    dt_object = datetime.fromtimestamp(time.time())
    print(dt_object)
    for input_value in range(process_count):
        process = Process(target=key_search, args=(p, g, X, Y, input_value, process_count))
        processes.append(process)
        process.start()

    for process in processes:
            process.join()
