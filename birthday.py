from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = "Friend"
input('Enter anything after scanning QR code')
time.sleep(5)
search = driver.find_element_by_class_name('_2zCfw')
search.click()
search.send_keys(name)
search.send_keys(Keys.RETURN)
msg_box = driver.find_element_by_class_name('_3u328')
while(time.localtime()[3]!=23):
    continue
while(time.localtime()[4]!=59):
    continue
while(time.localtime()[5]!=59):
    continue
msg_box.send_keys("Happy Birthday Amigo! Live Long! Party tomorrow.... ;)")
msg_box.send_keys(Keys.RETURN)
