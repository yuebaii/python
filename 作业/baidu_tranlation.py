#/usr/bin/env python
#coding=utf8
 
import http.client
import hashlib
import urllib.parse
import urllib.request
import random
import json
appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'

while(1):
    fromLanguage = input("请输入翻译前的语言类型:")
    toLanguage = input("请输入翻译后的语言类型:")
    words = input("请输入文字:")
    
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = words
    fromLang = fromLanguage
    toLang = toLanguage
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5(sign.encode(encoding='gb2312'))
#m1.update(sign)
#signs = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.request.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+m1.hexdigest()
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
        response = httpClient.getresponse()
        reader = response.read().decode('unicode-escape')
        data = json.loads(reader)
    
        print (data["trans_result"][0]["dst"])

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
