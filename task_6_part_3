import time
import requests
import sys
from threading import Thread
from urllib.parse import urlparse

start = time.time()
def get_html(link):
	text = requests.get(link)
	text.text
	print(f'{urlparse(link).hostname}')
urls = ['https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests?ysclid=l90c4r6o2s679264207',
		'https://python-scripts.com/requests?ysclid=l90b7e3b71835109648',
		'https://python-scripts.com/json?ysclid=l90d5ig492551599201',
		'https://translate.yandex.ru/',
		'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0']

threads = [Thread(target = get_html, args = (urls[i], )) for i in range(5)]

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
def get_html(link):
	text = requests.get(link)
	text.text
	print(f'{urlparse(link).hostname}')
urls = ['https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests?ysclid=l90c4r6o2s679264207',
		'https://python-scripts.com/requests?ysclid=l90b7e3b71835109648',
		'https://python-scripts.com/json?ysclid=l90d5ig492551599201',
		'https://translate.yandex.ru/',
		'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0']

threads = [Thread(target = get_html, args = (urls[i], )) for i in range(5)]

for t in threads:
	t.start()

for t in threads:
	t.join()

end = time.time()
print(f'Время выполнение параллельного запуска: {end - start}')
