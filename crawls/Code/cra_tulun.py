import requests
url = "http://www.tulun1024.com/TL001/"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:5000])
except:
    print("爬取失败")
