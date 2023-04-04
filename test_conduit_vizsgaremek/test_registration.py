from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from general_data import user

class TestConduit(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://localhost:1667/"
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()


# ATC002 - Regisztráció helyes adattal
    def test_registration(self):
        sign_up_button = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_button.click()

        username_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

        username_input.send_keys(user["name"])
        email_input.send_keys(user["email"])
        password_input.send_keys(user["password"])

        sign_up_button2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button2.click()

        registration_message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        registration_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert registration_message.text == "Welcome!"
        assert registration_problem.text == "Your registration was successful!"

        registration_ok_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        registration_ok_button.click()

        user_profile = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="nav-link"]')))[2]
        assert user_profile.text == user["name"]