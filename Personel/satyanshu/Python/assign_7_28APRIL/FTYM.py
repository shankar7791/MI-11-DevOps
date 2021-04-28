
def time():
	import time
	t = time.localtime()
	current_time = time.strftime("%H:%M", t)
	print(current_time)
time()
