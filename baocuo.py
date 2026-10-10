import urllib.request
import urllib.error
import socket


url = 'https://www.python.com/'
try:
    response = urllib.request.urlopen(url=url,timeout=0.01)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as error:
    if isinstance(error.reason, socket.timeout):
        print('当前任务已超时，即将执行下一任务！')