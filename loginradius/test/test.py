import unittest
from selenium import webdriver
import time
class DemoTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('.\chromedriver.exe')
        self.browser=webdriver.Firefox()
        self.mailid="<MAIL ID>"#replace the new mail id
        self.pwd="<PASSWORD>"#replace the test password
        self.addCleanup(self.browser.quit)
    
    def test_a_page_url(self): #Testing the Url of Two main pages using Their Title
        
        self.browser.get('http://127.0.0.1:8000/')
        print(f"---Visted----http://127.0.0.1:8000/-------{self.browser.title}----- ")
        self.assertEqual('Mainpage', self.browser.title)
        self.browser.get('http://127.0.0.1:8000/dashboard')
        print(f"---Visted----http://127.0.0.1:8000/dashboard-------{self.browser.title}-----case studey In this it will load mainpage beacause of no login is done and directly requesting dashboard URL")
        self.assertEqual('Mainpage',self.browser.title)
        print("Test1 success")
        
    def test_b_button(self):#Testing button wether its working and pointing the function in js
        
        self.browser.get('http://127.0.0.1:8000/')
        mainpage_c=self.assertEqual('Mainpage',self.browser.title)
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_id("fgt_btn").click()
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_id("reg_btn").click()       
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.find_element_by_id("login_btn").click()
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        print("Test2 success")
        
    def test_c_registeration_page(self):#Testing the Registration page step by step and used sleep function to load the content of webpage
        
        self.browser.get('http://127.0.0.1:8000/')
        self.assertEqual('http://127.0.0.1:8000/',self.browser.current_url)
        self.browser.find_element_by_id("reg_btn").click()
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        self.assertEqual('https://opdemo.hub.loginradius.com/auth.aspx?action=register&return_url=http://127.0.0.1:8000/register/auth',self.browser.current_url)
        time.sleep(5)
        self.browser.find_element_by_id("loginradius-registration-emailid").send_keys(self.mailid)
        self.browser.find_element_by_id("loginradius-registration-password").send_keys(self.pwd)
        self.browser.find_element_by_id("loginradius-submit-register").click()
        time.sleep(5)
        alert = self.browser.switch_to.alert
        alert.accept()
        time.sleep(5)
        self.assertEqual('http://127.0.0.1:8000/',self.browser.current_url)
        print("Test3 success")

    def test_d_login_page(self):#Testing the login page step by step and used sleep function to load the content of webpage
        
        self.browser.get('http://127.0.0.1:8000/')
        self.assertEqual('http://127.0.0.1:8000/',self.browser.current_url)
        self.browser.find_element_by_id("login_btn").click()
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        self.assertEqual('https://opdemo.hub.loginradius.com/auth.aspx?action=login&return_url=http://127.0.0.1:8000/login/auth',self.browser.current_url)
        self.browser.find_element_by_id("loginradius-login-emailid").send_keys(self.mailid)
        self.browser.find_element_by_id("loginradius-login-password").send_keys(self.pwd)
        self.browser.find_element_by_id("loginradius-submit-login").click()
        print(f"This is the current dashboar{self.browser.current_url}")
        time.sleep(5)
        alert = self.browser.switch_to.alert
        alert.accept()
        Stored_data=self.browser.execute_script("window.localStorage;")
        time.sleep(5)
        print(f"Stored:{Stored_data}")
        self.assertEqual('Dashboard',self.browser.title)
        print("Test4 success")
    
 
    def test_e_forgott_password_page(self):#Testing the Registration page step by step and used sleep function to load the content of webpage
        
        self.browser.get('http://127.0.0.1:8000/')
        self.assertEqual('http://127.0.0.1:8000/',self.browser.current_url)
        self.browser.find_element_by_id("fgt_btn").click()
        self.assertEqual('Login Register And Forgot Password',self.browser.title)
        self.assertEqual('https://opdemo.hub.loginradius.com/auth.aspx?action=forgotpassword&return_url=http://127.0.0.1:8000/fp/auth',self.browser.current_url)
        time.sleep(5)
        self.browser.find_element_by_id("loginradius-forgotpassword-emailid").send_keys(self.mailid)
        self.browser.find_element_by_id("loginradius-submit-send").click()
        time.sleep(5)
        alert = self.browser.switch_to.alert
        print(alert.text)
        alert.accept()
        time.sleep(5)
        self.assertEqual('http://127.0.0.1:8000/',self.browser.current_url)
        print("Test5 success")
        
if __name__ == '__main__':
    unittest.main()