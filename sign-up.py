#!/usr/local/opt/python/bin/python3.7
from selenium import webdriver
import time

dID = input("Username:")
pswd = input("Password:")
UID = input("UID:")

options_ = webdriver.ChromeOptions()
options_.add_argument("user-data-dir=/Users/matthewwong/Library/Application Support/Google/Chrome")

chromedriver = '/usr/local/bin/chromedriver'

browser = webdriver.Chrome(chromedriver, options=options_)
browser.get('https://www.imleagues.com/spa/account/login')

time.sleep(5)

school_dropdown_btn = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/button")
school_dropdown_btn.click()

time.sleep(3)

umd_list_item = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/ul/li[1743]")
umd_list_item.click()

time.sleep(15)

reservation_link = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[9]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/a[2]")
reservation_link.click()

time.sleep(7)

tomorrow_page = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[11]")
tomorrow_page.click()

time.sleep(8)

#2:30 Section

signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[18]/a/div/div[2]/div[1]/button")
signup_btn.click()

# Test
#signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[12]/a/div/div[2]/div[1]/button")
#signup_btn.click()

time.sleep(5)

enter_uid = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
enter_uid.send_keys(UID)

final_signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button")
final_signup_btn.click()

browser.quit()
