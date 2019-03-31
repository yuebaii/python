import requests
import re
from urllib.parse import urlencode
from requests import codes
from hashlib import md5
import os

headers = {
    'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebKit/537.36(KHTML,like Gecko) '
                  'Chrome/65.0.3325.162 Safari/537.36'
}


# http://www.xmeitongs.com/plugin.php?id=xlwsq_tuku&mod=list&page=2
def get_page(offset):
    params = {
        'id': 'xlwsq_tuku',
        'mod': 'list',
        'page': offset
    }

    base_url = 'http://www.xmeitongs.com/plugin.php?'
    url = base_url + urlencode(params)

    try:
        resp = requests.get(url, headers=headers)
        print(url)
        if 200 == resp.status_code:
            print("succ0")
            return resp.text
    except requests.ConnectionError:
        return None


def get_images(html):
    print("succ1")
    pattern = re.compile('<li class="listbox".*?<a href="(.*?)".*?</a>', re.S)
    items = re.findall(pattern, html)
    # print(items)

    for item in items:
        url = 'http://www.xmeitongs.com/' + item
        # print(url)
        try:
            htmls = requests.get(url, headers=headers)
            print(htmls)
            if 200 == htmls.status_code:
                print("succ2")
                # return htmls
        except requests.ConnectionError:
            return None

        patterns = re.compile('<li><img id="(.*?)".*?src="(.*?)".*?</li>', re.S)
        patternss = re.compile('<div style="float:left;">(.*?)</div>', re.S)
        hrefs = re.findall(patterns, htmls.text)
        hrefss = re.findall(patternss, htmls.text)

        for href in hrefs:
            urls = 'http://www.xmeitongs.com/' + href[1]

            img_path = 'imgs' + os.path.sep + str(hrefss)
            print('succ3')
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            try:
                resp = requests.get(urls)
                if 200 == resp.status_code:
                    file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                        file_name=md5(resp.content).hexdigest(),
                        file_suffix='jpg')
                    if not os.path.exists(file_path):
                        with open(file_path, 'wb') as f:
                            f.write(resp.content)
                        print('Downloaded image path is %s' % file_path)
                        print('succ4')
                    else:
                        print('Already Downloaded', file_path)
            except requests.ConnectionError:
                print('Failed to Save Image，item %s' % item)
    # print("succ22")


# def parse_images(item):


# def save_image(item):


def main():
    for offset in range(1, 11):
        html = get_page(offset)
        get_images(html)


if __name__ == '__main__':
    main()