from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

def account_info():
    with open('account_info.text', 'r') as f:
        info = f.read().split()
        number = info[2]
        password = info[3]
    return number, password

number, password = account_info()

options = Options()
options.add_argument('start-maxsized')
driver = webdriver.Chrome(options=options)

driver.get('https://www.instagram.com/accounts/login/?hl=en')

username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
login_xpath = '//*[@id="loginForm"]/div/div[3]'

time.sleep(2)

driver.find_element_by_xpath(username_xpath).send_keys(number)
time.sleep(0.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5)
driver.find_element_by_xpath(login_xpath).click()

'''
message = chrome.find_element_by_class_name('_862NM ')
message.click()
time.sleep(2)
chrome.find_element_by_class_name('HoLwm ').click()
time.sleep(1)
l = ['hello', 'Hi', 'How are You', 'Hey', 'Bro whats up'] #will take this input
for x in range(10):
    mbox = chrome.find_element_by_tag_name('textarea')
    mbox.send_keys(random.choice(l))
    mbox.send_keys(Keys.RETURN)
    time.sleep(1.2)
    '''
