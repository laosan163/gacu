import urllib.request
import urllib.parse
import http.cookiejar
import json
import ssl
import re
from http.cookiejar import CookieJar

# -------------------------- SSL配置（解决证书验证失败） --------------------------
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# CookieJar：自动保存、携带所有Cookie，不用手动解析Set-Cookie
cookie_jar = CookieJar()
from urllib import response

from django.http import cookie

url = 'https://github.com/login'
data =bytes(urllib.parse.urlencode({'username': 'laosan163', 'password': '780929xia'}), encoding='utf-8')
cookie =http.cookiejar.CookieJar()
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_processor)
response = opener.open(url, data=data)
response = json.loads(response.read().decode("utf-8"))['msg']
if response=='登录成功！':
    for i in cookie:
        print(i.name+'='+i.value)
