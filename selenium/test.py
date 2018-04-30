from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
base_url = "http://www.facebook.com"

driver.get(base_url)

driver.find_element_by_name('email').send_keys('rjcostales@mac.com')
driver.find_element_by_name('pass').send_keys('rJsC1024')
driver.find_element_by_id('loginbutton').click()
