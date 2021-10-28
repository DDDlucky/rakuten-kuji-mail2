from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

user_name = 'silent_quiet_d@yahoo.co.jp'
user_passwd = 'do1123'

def Operation(url, user_name, user_passwd):
    op = Options()
    op.add_argument("--no-sandbox")
    op.add_argument('--disable-dev-shm-usage')
    op.add_argument('--headless')
    driver = webdriver.Chrome(options=op)

    driver.get(url)
    driver.implicitly_wait(20)
    driver.find_element_by_id('loginInner_u').send_keys(user_name)
    driver.find_element_by_id('loginInner_p').send_keys(user_passwd)
    driver.find_element_by_class_name('loginButton').click()

    mail_num = len(driver.find_elements_by_xpath('//div[@class="listCont"]/a'))
    driver.implicitly_wait(20)
    for i in range(mail_num):
        if 'grp13' not in driver.find_elements_by_xpath('//div[@class="listCont"]/a')[i].get_attribute('href'):
            driver.find_elements_by_xpath('//div[@class="listCont"]/a')[i].click()
            driver.implicitly_wait(20)
            driver.find_element_by_class_name('point_url').click()
            driver.back()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)
            driver.back()

    driver.quit()

def main():
    Operation('https://member.pointmail.rakuten.co.jp/box', user_name, user_passwd)

if __name__ == '__main__':
    main()
