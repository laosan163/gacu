import urllib.request
import urllib.parse
import ssl
import re

# 关闭ssl校验
ssl._create_default_https_context = ssl._create_unverified_context

url_login_page = "https://github.com/login"
url_submit = "https://github.com/session"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# 第一步：GET登录页，获取csrf token和cookie
req_get = urllib.request.Request(url_login_page, headers=headers)
resp_get = urllib.request.urlopen(req_get)
html = resp_get.read().decode('utf-8')

# 正则提取 authenticity_token
pattern = r'authenticity_token.*?value="(.*?)"'
token = re.search(pattern, html).group(1)
print("拿到csrf token:", token)

# 表单字段：github的字段名是 login, password
post_data = urllib.parse.urlencode({
    'login': 'laosan163',
    'password': '780929xia',
    'authenticity_token': token
}).encode('utf-8')

# 带上之前的Cookie
headers["Cookie"] = resp_get.info().get('Set-Cookie')

req_post = urllib.request.Request(url_submit, data=post_data, method="POST", headers=headers)
try:
    resp = urllib.request.urlopen(req_post)
    print(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print("错误码：", e.code)
    print(e.read().decode('utf-8'))
