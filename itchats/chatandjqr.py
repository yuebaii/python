import requests
keyword = "爬虫"
KEY = 'bfaddb5c7af1404fb016373fc5669339'
api = 'http://www.tuling123.com/openapi/api?key=' + KEY + '&info='

while True:
    info = input('我: ')  
    request = api + info  
    r = requests.get(request)
    r.raise_for_status()
    print(r.text)
    
