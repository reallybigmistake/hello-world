numconsumers = 2
numproducers = 4
nummessages = 10
import threading, queue, time
safeprint = threading.Lock()
dataQueue = queue.Queue()
def producer(idnum):
	for msgnum in range(nummessages):
		time.sleep(idnum)
		dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))
def consumer(idnum):
	while True:
		time.sleep(idnum)
		try:
			data = dataQueue.get(block=False)
		except queue.Empty:
			pass
		else:
			with safeprint:
				print('consumer', idnum, 'got=>', data)

if __name__ == '__main__':
	for i in range(numconsumers):
		thread = threading.Thread(target=consumer, args=(i,))
		thread.daemon = True # else cannot exit!
		thread.start()
	waitfor = []
	for i in range(numproducers):
		thread = threading.Thread(target=producer, args=(i,))
		waitfor.append(thread)
		thread.start()
	for thread in waitfor: thread.join() # or time.sleep() long enough here
	print('Main thread exit')
