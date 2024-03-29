import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Hosttest(LiveServerTestCase):



    def test_homepage(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.live_server_url)


        time.sleep(1)
        assert 'Hello, world!' in driver.title
        driver.quit()


# class LoginFormTest(LiveServerTestCase):

#     def testform(self):
#         driver = webdriver.Chrome()
#         driver.get('http://127.0.0.1:8000/accounts/login/')
#         time.sleep(1)

#         username =  driver.find_element(By.NAME, 'username')
#         password =  driver.find_element(By.NAME, 'password')
#         submit = driver.find_element(By.ID, 'submit')

#         username.send_keys('hagp')
#         password.send_keys('admin')
#         time.sleep(1)

#         submit.send_keys(Keys.RETURN)

#         assert 'hagp' in driver.page_source
        
#         time.sleep(5)
#         driver.close()
