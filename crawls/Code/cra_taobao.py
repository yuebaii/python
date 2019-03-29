import re
import requests

def GetHtmlText(url):
    try:
        r = requests.get(url, timeout = 25)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def ParsePage(lists, html):
    try:
        z = re.findall(r'\"view_price\"\:\".*?\"', html)
        zz = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(z)):
            price = eval(z[i].split(':')[1])
            name = eval(zz[i].split(':')[1])
            lists.append([price, name])
    except:
        print("")
        
def PrintGoodlist(lists):
    muban = "{:4}\t{:8}\t{:16}"
    print(muban.format("序号","价格","商品名称"))
    count = 0
    for g in lists:
        count = count +1
        print(muban.format(count,g[0],g[1]))

def main():
    goods = '书包'
    start_url = "https://s.taobao.com/search?q=" + goods
    depth = 3
    uinfo = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = GetHtmlText(url)
            ParsePage(uinfo, html)
        except:
            continue

    PrintGoodlist(uinfo)
main()



                  
        
    
