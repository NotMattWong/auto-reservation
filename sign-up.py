#!/usr/local/opt/python/bin/python3.7
from selenium import webdriver
import time

dID = input("Directory ID:")
pswd = input("Password:")
UID = input("UID:")

# Loading Default Google Chrome User Profile to ChromeDriver
options_ = webdriver.ChromeOptions()
options_.add_argument("user-data-dir=/Users/matthewwong/Library/Application Support/Google/Chrome")

# Load new instance of Chrome with User Profile and open login link to UMD Recwell
browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=options_)
browser.get('https://www.imleagues.com/spa/account/login')

time.sleep(5)

# Click Dropdown Menu
school_dropdown_btn = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/button")
school_dropdown_btn.click()

time.sleep(3)

# Click UMD for login
umd_list_item = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/ul/li[1743]")
umd_list_item.click()

time.sleep(15)

# Click Reservations Tab
reservation_link = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[9]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/a[2]")
reservation_link.click()

time.sleep(7)

# Click on the next day
tomorrow_page = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[11]")
tomorrow_page.click()

time.sleep(8)

# Sign Up for the 2:30 Section
signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[18]/a/div/div[2]/div[1]/button")
signup_btn.click()

time.sleep(5)

# Enter UID into input box
enter_uid = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
enter_uid.send_keys(UID)

# Click Sign Up
final_signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button")
final_signup_btn.click()

# Close Instance of Chrome
browser.quit()
