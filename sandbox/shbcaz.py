import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def move_off(self):
    ActionChains(self).move_by_offset(0, 20).perform()


driver = webdriver.Firefox()
driver.implicitly_wait(10)
base_url = "http://www.shbcaz.org/"

driver.get(base_url + "index.html")
driver.set_window_size(800, 1000)
time.sleep(1)

driver.find_element_by_link_text("Church").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/ul/li[1]/ul/li/a").click()
time.sleep(1)

driver.find_element_by_link_text("Sunday School").click()
time.sleep(1)
driver.find_element_by_link_text("Junior Church").click()
time.sleep(1)

driver.find_element_by_link_text("Sunday School").click()
time.sleep(1)
driver.find_element_by_link_text("Youth Ministry").click()
time.sleep(1)

# driver.find_element_by_link_text("Missions").click()
# # move_off(driver)
# time.sleep(1)

# driver.find_element_by_link_text("About Us").click()
# # move_off(driver)
# time.sleep(1)

driver.get_screenshot_as_file("shbcaz.png")
time.sleep(1)

driver.quit()
