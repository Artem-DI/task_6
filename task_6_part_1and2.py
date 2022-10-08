import time
import sys
from threading import Thread

print('\n')
d = ['book', 'door', 'Rob', 'sleep', 'cockpit']

start = time.time()

def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

threads = [Thread(target = get_thread, args = (i, )) for i in d]

for t in threads:
	t.start()
	t.join()
end = time.time()
print(f'Время выполнение последовательного запуска: {end - start}')

for i in ('\n/////////////////////////////////////////////////////////////\n\n'):
	time.sleep(0.01)
	sys.stdout.write(i)
	sys.stdout.flush()

start = time.time()
def get_thread(thread_name):
	time.sleep(1)
	print(thread_name)

threads = [Thread(target = get_thread, args = (i, )) for i in d]

for t in threads:
	t.start()
for i in threads:
	t.join()
end = time.time()
print(f'Время выполнение параллельного запуска: {end - start}')