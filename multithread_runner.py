import time
import threading
from serial_random import fn

if __name__ == '__main__':
	st = time.time()
	size = 1000000
	threads = 10
	jobs = []
	for i in range(0, threads):
		l = list()
		thread = threading.Thread(target=fn(size, l, i))
		jobs.append(thread)
	
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()

	print('Multi-thread processing finished ...')
	elapsed = time.time() - st
	print(f'multi-thread processing = {elapsed}')