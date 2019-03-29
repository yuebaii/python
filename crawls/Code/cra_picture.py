import requests
import os

url = "http://img0.dili360.com/rw17/ga/M02/44/50/wKgBy1eppriAJO1gACWy8cG55A4558.tub.jpg"
root = "E://picss//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
    else:
        print("文件已存在")
except:
    print("爬取失败")
    
