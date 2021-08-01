from django.test import TestCase,Client
from django.urls import resolve
from .views import home
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Create your tests here.

class UnitTest(TestCase):

    def test_main_url_exists(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_return_main_html(self):
        response = Client().get("")
        self.assertTemplateUsed(response, "account/home.html")

    def test_main_view_func(self):
        found = resolve("/")
        self.assertEqual(found.func, home)


class FunctionalTest(TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')

        self.driver  = webdriver.Chrome()
        super(FunctionalTest, self).setUp()

    def test_story10_url(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')

    def test_story10_sign_up_and_check_redirect(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "greet_not_log_in")))
        signup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "register")))
        signup.click()
        driver.implicitly_wait(10)
        username = driver.find_element_by_id('id_username')
        username.send_keys("TestingUser123")
        password1 = driver.find_element_by_id('id_password1')
        password1.send_keys("godofwar007")
        password2 = driver.find_element_by_id('id_password2')
        password2.send_keys("godofwar007")
        button = driver.find_element_by_id('signup_btn')
        button.click()
        
        login_username = driver.find_element_by_id('id_username')
        login_password = driver.find_element_by_id('id_password')
        login_username.send_keys("TestingUser123")
        login_password.send_keys("godofwar007")
        login_button = driver.find_element_by_id('login_btn')
        login_button.click()
        driver.implicitly_wait(10)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "greet_log_in")))

    def tearDown(self):
        self.driver.quit()
        super(FunctionalTest, self).tearDown()

