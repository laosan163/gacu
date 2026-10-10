import urllib.request       #导入urllib.request模块
#import ssl
import urllib.error
import gzip
import requests
import socket
from urllib import response

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.python.org/'
try:
    response = urllib.request.urlopen(url=url,timeout=0.1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as error:
    if isinstance(error.reason, socket.timeout):
        print('当前任务已超时，即将执行下一任务！')