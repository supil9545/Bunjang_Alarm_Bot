import requests
from bs4 import BeautifulSoup
import os
import telegram
from selenium import webdriver
import time
from multiprocessing import Pool

def bunjang():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument("lang=ko_KR")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    bot = telegram.Bot(token = '')

    chat_id = bot.getUpdates()[-1].message.chat.id

    driver = webdriver.Chrome('/Users/user/Downloads/\chromedriver_win32/chromedriver', options = options)

    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")

    while True:

        driver.implicitly_wait(3)
        driver.get('https://m.bunjang.co.kr/search/products?q=%EA%B0%A4%EB%9F%AD%EC%8B%9C%ED%83%ADs7%20%2B')
        latest = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[5]/div/div[4]/div/div[2]/a/div[2]/div[1]').text

        try:
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
                before = f_read.readline()
                if before != latest:
                    bot.sendMessage(chat_id = chat_id, text = '새 글이 올라왔어요!')
                else:
                    bot.sendMessage(chat_id = chat_id, text = '새 글이 없어요 ㅠㅠ')
                f_read.close()

            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
                f_write.write(latest)
                f_write.close()

        except:
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f:
                f.write(latest)

        time.sleep(10)
'''        while(True):
            pass '''



if __name__ == '__main__':
    pool = Pool(processes=8) # 4개의 프로세스를 사용합니다.
    pool.map(bunjang()) # get_contetn 함수를 넣어줍시다
