#first install selenium using - "!pip install selenium"  in console
#then this- "!pip install webdriver_manager"
#then install webdriver, by clicking - http://selenium-python.readthedocs.io/installation.html#drivers


#Task- to submit code of problem- https://www.codechef.com/submit/TEST

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.codechef.com/")

username_element=browser.find_element_by_id("edit-name")

username_element.send_keys("Enter Email id here")

password_element=browser.find_element_by_id("edit-pass")
password_element.send_keys("Enter pass here")

time.sleep(4)

browser.find_element_by_id("edit-submit").click()

time.sleep(3)

browser.get("https://www.codechef.com/submit/TEST")

with open("Solution.cpp") as f:
    code=f.read()


code_element=browser.find_element_by_id("result")
code_element.send_keys(code)

time.sleep(8)

browser.find_element_by_id("edit-number-1").click()


