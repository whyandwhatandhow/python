from bs4 import BeautifulSoup
import requests

url = "https://baidu.com"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Content-Type': 'application/json;charset=UTF-8'
}

response = requests.get(url=url, headers=header)
response.encoding = 'utf-8'
text = response.text

soup = BeautifulSoup(text, 'html.parser')  # 指定解析器为html

links = soup.find_all("a")

for i in links:
    print(i.get("href"))
