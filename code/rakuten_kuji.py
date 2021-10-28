from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

user_name = 'silent_quiet_d@yahoo.co.jp'
user_passwd = 'do1123'

def play(url):
    op = Options()
    op.add_argument("--no-sandbox")
    op.add_argument('--disable-dev-shm-usage')
        op.add_argument('--headless')
    driver = webdriver.Chrome(options=op)

    driver.get(url)
    try:
        driver.implicitly_wait(5)
        driver.find_element_by_id('loginInner_u').send_keys(user_name)
        driver.find_element_by_id('loginInner_p').send_keys(user_passwd)
        driver.find_element_by_class_name('loginButton').click()
    except:
        pass
    driver.implicitly_wait(5)
    try:
        driver.find_element_by_id('entry').click()
        time.sleep(30)
    except:
        pass

    driver.quit()

def Operation(url):
    op = Options()
    op.add_argument("--no-sandbox")
    op.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=op)

    driver.get(url)
    driver.implicitly_wait(20)
    kuji_urls = []
    for kuji in driver.find_elements_by_xpath('//section[@class="kuji_list"]/ul/li/a'):
        kuji_urls.append(kuji.get_attribute('href'))

    driver.quit()

    return kuji_urls

def main():
    urls = Operation('https://kuji.rakuten.co.jp/')
    for url in urls:
        play(url)

if __name__ == '__main__':
    main()
