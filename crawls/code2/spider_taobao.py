
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote

browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
MAX_PAGE = 10
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
'''
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
wait = WebDriverWait(browser, 25)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
KEYWORD = 'iPad'

def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        print('-1')
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form> input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form> span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active> span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        print('0')
        get_products()

    except TimeoutException:
        print("time out")
        index_page(page)

def get_products():
    print('1')
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print('2')
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()

'''
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import csv

driver = webdriver.Chrome()
# driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
url = 'https://www.taobao.com/'
driver.get(url)

driver.find_element_by_xpath('//*[@id="q"]').send_keys('iPad')
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
with open('iPad.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(('商品', '价格', '店铺'))

while True:
    divs = driver.find_elements_by_xpath('//div[contains(@class, "J_MouserOnverReq")]')
    for div in divs:
        shop = div.find_element_by_xpath('.//div[2]/div[3]/div[1]').text
        goods = div.find_element_by_xpath('.//div[2]/div[2]/a').text.strip()
        price = div.find_element_by_xpath('.//div[2]/div[1]/div[1]').text
        with open('iPad.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow((goods, price, shop))

    try:
        next_page = driver.find_element_by_xpath('//a[contains(@trace, "srp_bottom_pagedown")]')
    except NoSuchElementException as e:
        print('爬取完毕！')
        break
    else:
        time.sleep(4)
        print('开始爬取第{}页'.format(driver.find_element_by_xpath('//li[@class="item active"]').text))
        next_page.click()
        time.sleep(3)
        driver.refresh()

driver.quit()
'''
