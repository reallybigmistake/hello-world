"Spawn threads until you type 'q'"
import _thread, time
def counter(myId, count):
	for i in range(count):
		time.sleep(1)
		mutex.acquire()
		print('[%s] => %s' % (myId, i))
		mutex.release()
mutex = _thread.allocate_lock()
for i in range(5):
	_thread.start_new_thread(counter, (i, 5))
time.sleep(6)
print('Main thread exiting')
