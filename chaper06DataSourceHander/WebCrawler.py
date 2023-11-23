import requests


url="https://www.xuexi.cn/"
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Content-Type':'application/json;charset=UTF-8'
}


response=requests.get(url=url,headers=header,verify=False,auth=False,proxies=False)
response.encoding='utf-8'
print(response.text)



#r=request.headers#看头
# request.content#以字节方式返回内容
# request.encoding
# request.text()
# r.cookies

