import requests
url = "https://www.amazon.cn/gp/product/B005WGDGB2/ref=zg_bs_755653051_2?ie=UTF8&psc=1&refRID=5KQNKNG4BMBGGS0HA9FP"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败！")
