import requests
keyword = "爬虫"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(r.text)
except:
    print("爬取失败！")
