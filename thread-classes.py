import threading
def action(i):
	def power():
		print(i ** 32) 
	return power
threading.Thread(target=(lambda:action(2))).start()