import time

from selenium import webdriver
# create a new Firefox session
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

# navigate to the application home page
# driver.get("https://ols-qa3.ubstest.net")
driver.get("https://ols-dev2.ubsdev.net")


def login(user_id):
    username = driver.find_element_by_id("username")
    username.clear()
    time.sleep(3)

    username.send_keys(user_id)
    time.sleep(3)

    password = driver.find_element_by_id("password")
    password.send_keys("sigfig123")
    time.sleep(3)

    submit = driver.find_element_by_id("submit")
    submit.submit()
    time.sleep(60)

    driver.get("https://ols-qa3.ubstest.net/wma/sigfig")
    time.sleep(200)

    logout = driver.find_element_by_link_text("Log Out")
    logout.click()
    time.sleep(60)


virgin = ['sf158_866294200', 'sf168_727842400', 'sf201_7490602100', 'sf242_1501267000', 'sf525_8569326400',
          'sf541_715734400', 'sf577_3531405300', 'sf827_6788648000', 'sf988_6720997000', 'sf1569_836934400',
          'sf1646_6799806100', 'sf2215_4068557400', 'sf3637_5926321100', 'sf3651_6800931200', 'sf3656_7535286400',
          'sf3661_8014886400', 'sf3675_7383446400', 'sf3676_9889534300', 'sf3678_732226000']

active = ['sf137_8315839000', 'sf203_4798901000', 'sf210_1989736000', 'sf224_1022276100', 'sf704_7761121000',
          'sf1682_886872400', 'sf3659_3639867100', 'sf3668_6841162200', 'sf3671_7063907300', 'sf3672_6899464300']

error = ['sf173_8209672000', 'sf196_9729308000', 'sf207_7482340200', 'sf2053_1057066400', 'sf1662_5567312000',
         'sf3670_2233166400', 'sf1483_7992110100']

for user_id in ['sf137_8315839000', 'sf203_4798901000']:
    try:
        login(user_id)
        print('GOOD', user_id)
    except NoSuchElementException:
        print('FAIL', user_id)
        pass

driver.close()
print('DONE')
