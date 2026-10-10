import urllib.request         #导入urllib.request模块
import urllib.parse           #导入urllib.parse模块
import ssl

# 关闭SSL证书校验，仅本地爬虫调试用
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.httpbin.org/post'
#将表单数据转换为bytes类型，并设置编码为utf-8
data = bytes(urllib.parse.urlencode({'hello': 'python'}), encoding='utf-8')

# 把timeout从0.1修改为10
response = urllib.request.urlopen(url=url, context=ctx, data=data, timeout=1)
print(response.read().decode('utf-8'))
