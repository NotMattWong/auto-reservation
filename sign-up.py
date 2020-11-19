#!/usr/local/opt/python/bin/python3.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

# School Name
school = 'university of maryland'

# School Credentials
dID = input("Directory ID:")
pswd = input("Password:")
UID = input("UID:")

# Loading Default Google Chrome User Profile to ChromeDriver
options_ = webdriver.ChromeOptions()
options_.add_argument("user-data-dir=/Users/matthewwong/Library/Application Support/Google/Chrome")

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

time.sleep(15)

# Click Reservations Tab
reservation_link = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[9]/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/a[2]")
reservation_link.click()

time.sleep(7)

# Date Picker
def day(i):
    switcher = {
        0:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[9]",
        1:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[10]",
        2:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[11]",
        3:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[12]",
        4:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[13]",
        5:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[14]",
        6:"/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[2]/div/div[8]",
    }
    return switcher.get(i, "Date Picker Messed Up")

if(datetime.datetime.today().weekday() + 1 > 6):
    currDay = -1
else:
    currDay = datetime.datetime.today().weekday()

# Click on the next day
tomorrow_page = browser.find_element_by_xpath(day(currDay + 1))
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
