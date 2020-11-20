#!/usr/local/opt/python/bin/python3.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os

# School Name
school = 'university of maryland'

# School Credentials
dID = input("Directory ID:")
pswd = input("Password:")
UID = input("UID:")

# Start Duo Authenticator Phone
os.system('/Users/matthewwong/Library/Android/sdk/platform-tools/adb kill-server')
os.system('/Users/matthewwong/Library/Android/sdk/platform-tools/adb start-server')
os.system('/Users/matthewwong/Library/Android/sdk/emulator/emulator -avd Gym_Signup_Phone -no-snapshot-load &')

time.sleep(20)

# Loading Default Google Chrome User Profile to ChromeDriver
options_ = webdriver.ChromeOptions()
options_.add_argument("user-data-dir=/Users/matthewwong/Library/Application Support/Google/Chrome")
options_.add_argument("--disable-popup-blocking")

# Load new instance of Chrome with User Profile and open login link to UMD Recwell
browser = webdriver.Chrome('/usr/local/bin/chromedriver', options=options_)
browser.get('https://www.imleagues.com/spa/account/login')

time.sleep(10)

# Click Dropdown Menu
school_dropdown_btn = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/button")
school_dropdown_btn.click()

time.sleep(3)

# Type UMD and enter for login
enter_school = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/div/input")
enter_school.send_keys(school)
enter_school.send_keys(Keys.ENTER)

time.sleep(10)

# DUO Login

# Directory ID
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[1]/input").send_keys(dID)
# Password
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[2]/input").send_keys(pswd)
# Login Button
browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[4]/button").click()

time.sleep(40)

# Click Reservations Tab
reservation_link = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[9]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/a[2]")
reservation_link.click()

time.sleep(7)

# Click on the next day
tomorrow_page = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/button[2]")
tomorrow_page.click()

time.sleep(8)

# Sign Up for the 2:30 Section
browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[18]/a/div/div[2]/div[1]/button").click()

# Test Case
# browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[16]/a/div/div[2]/div[1]/button").click()

time.sleep(5)

# Enter UID into input box
enter_uid = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/input")
enter_uid.send_keys(UID)

# Click Sign Up
final_signup_btn = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button")
final_signup_btn.click()

# Close Emulator
os.system('/Users/matthewwong/Library/Android/sdk/platform-tools/adb -s emulator-5554 emu kill')
os.system('/Users/matthewwong/Library/Android/sdk/platform-tools/adb kill-server')

# Close Instance of Chrome
browser.quit()
