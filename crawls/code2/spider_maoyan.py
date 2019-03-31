import requests
import re
import json
import  time

def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_3)AppleWebKit/537.36(KHTML,like Gecko) '
                     'Chrome/65.0.3325.162 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text

    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)'
                    '</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    #print(items)

    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'scorre':item[5]+item[6]
        }

def write_to_files(content):
    path = 'result.txt'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
  # parse_one_page(html)
    for items in parse_one_page(html):
        print(items)
        write_to_files(items)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
      # time.sleep(1)as


