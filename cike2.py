import urllib.request
import urllib.parse
import ssl
import re
from http.cookiejar import CookieJar

# -------------------------- SSL配置（解决证书验证失败） --------------------------
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# CookieJar：自动保存、携带所有Cookie，不用手动解析Set-Cookie
cookie_jar = CookieJar()

# 构建opener：Cookie处理器 + HTTPS忽略证书处理器
opener = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(cookie_jar),
    urllib.request.HTTPSHandler(context=ctx)
)
urllib.request.install_opener(opener)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# -------------------------- 第一步：GET访问登录页，拿authenticity_token --------------------------
url_login_page = "https://github.com/login"
req_get = urllib.request.Request(url_login_page, headers=headers)
try:
    resp_get = opener.open(req_get)
    html = resp_get.read().decode("utf-8")
except Exception as e:
    print("访问登录页面失败：", e)
    exit()

# 正则提取csrf token，增加捕获异常
token_match = re.search(r'authenticity_token.*?value="(.*?)"', html)
if not token_match:
    print("❌ 没有找到 authenticity_token，页面结构变了！")
    exit()
token = token_match.group(1)
print("✅ 获取到CSRF Token：", token[:50], "...")

# -------------------------- 第二步：POST提交登录表单 --------------------------
url_submit = "https://github.com/session"
post_form_data = {
    "login": "laosan163",
    "password": "780929xia",
    "authenticity_token": token
}
# 字典转表单bytes
post_data = urllib.parse.urlencode(post_form_data).encode("utf-8")

req_post = urllib.request.Request(url_submit, data=post_data, method="POST", headers=headers)
try:
    resp = opener.open(req_post)
    print("✅ 登录请求成功！状态码：", resp.getcode())
    print(resp.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"❌ HTTP Error, code={e.code}")
    print("服务器返回内容：")
    print(e.read().decode("utf-8"))
except Exception as e:
    print("❌ 其他异常：", e)
