from serial_random import fn
import time
import multiprocessing

if __name__ == '__main__':
    st = time.time()
    size = 10000000
    processes = 10
    jobs = []

    for i in range(0, processes):
        out_list = list()
        proc = multiprocessing.Process(target=fn, args=(size, out_list))
        jobs.append(proc)
    
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print('Multi-processing method complete ...')        
    elapsed = time.time() - st
    print(f'Multi-processing method took: {elapsed}')