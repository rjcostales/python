# /usr/bin/env python
import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
base_url = "http://shbcaz.org/"

driver.get(base_url + "index.html")

driver.find_element_by_link_text("Missions").click()
time.sleep(3)

driver.find_element_by_link_text("Sunday School").click()
time.sleep(3)

driver.find_element_by_link_text("Sunday School").click()
driver.find_element_by_link_text("Junior Church").click()
time.sleep(3)

driver.find_element_by_link_text("Sunday School").click()
driver.find_element_by_link_text("Youth Ministry").click()
time.sleep(3)
