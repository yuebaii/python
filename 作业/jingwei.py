import requests
import json
while (True):
    address = input('请输入地点:')
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    url = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(url, par)
    json_data = json.loads(res.text)
    geo = json_data['geocodes'][0]['location']
    longitude = geo.split(',')[0]
    latitude = geo.split(',')[1]
    print('位   置   :东经',longitude,'度','  ','南纬',latitude,'度')
