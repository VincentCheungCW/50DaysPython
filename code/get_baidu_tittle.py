from urllib.request import urlopen
from bs4 import BeautifulSoup

# http://www.baidu.com/
url = input("请输入url:")

# 请求获取HTML
html = urlopen(url)

# 用BeautifulSoup解析html
obj = BeautifulSoup(html.read(), 'html.parser')

title = obj.head.title.text
# 打印标题
print(title)
