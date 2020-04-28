from serial_random import fn
import time

if __name__ == '__main__':
    st = time.time()
    size = 10000000
    runs = 10
    
    for i in range(runs):
        l = list()
        fn(size, l)

    print('Serial processing finished ...')
    elapsed = time.time() - st
    print(f'serial processing = {elapsed}')
    
