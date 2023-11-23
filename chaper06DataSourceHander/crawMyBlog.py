import requests
from bs4 import BeautifulSoup

url="https://tf.icu/"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

response=requests.get(url=url,headers=headers)
response.encoding='utf-8'

html_doc=response.text

soup=BeautifulSoup(html_doc,"html.parser")

h2_nodes=soup.find_all("h2")

for h2_node in h2_nodes:
    link=h2_node.find("a")
    print(link['href'],link.get_text())
