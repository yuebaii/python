import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
#from multiprocessing.pool import Pool
import re

headers = {
    'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebKit/537.36(KHTML,like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'
}
#keyword=%E8%A1%97%E6%8B%8D
def get_page(offset):
    params = {
        'aid': '24',
        'app_name' : 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc':'1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url, headers = headers)
        print(url)
        if 200  == resp.status_code:
            print("succ0")
            return resp.json()
    except requests.ConnectionError:
            return None

def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                origin_image = re.sub("list", "origin", image.get('url')) #正则表达式的替换，即 image.get(url)里的list正则表达式替换为"origin"
                yield {
                    'image':  origin_image,
                   # 'iamge': image.get('url'),
                    'title': title
                }

#print('succ')

def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    print('succ2')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                print('succ3')
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
                print('succ4')
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def main():
    for offset in range(0,10):
        json = get_page(offset*20)

        for item in get_images(json):
           # print(item)
            save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    main()
    '''
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    '''