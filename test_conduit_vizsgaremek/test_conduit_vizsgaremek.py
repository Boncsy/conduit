from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv
from general_functions import login, create_article, create_comment
from general_data import user, article, comment


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



# ATC001 - Adatkezelési tájékoztató
    def test_accept_cookies(self):
        accept_button = self.browser.find_element(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
        accept_button.click()
        time.sleep(2)
        decline_button_list = self.browser.find_elements(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--decline"]')
        assert not len(decline_button_list)


# ATC003 - Regisztráció helytelen email címmel
    def test_registration1(self):
        sign_up_button = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_button.click()

        username_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

        username_input.send_keys(user["name"])
        email_input.send_keys('test@')
        password_input.send_keys(user["password"])

        sign_up_button2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button2.click()

        time.sleep(2)

        registration_message = self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')
        registration_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert registration_message.text == "Registration failed!"
        assert registration_problem.text == "Email must be a valid email."

        registration_failed_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        registration_failed_button.click()


# ATC004 - Regisztráció üres mező kitöltésekkel
    def test_registration2(self):
        sign_up_button = self.browser.find_element(By.LINK_TEXT, 'Sign up')
        sign_up_button.click()

        username_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

        username_input.send_keys()
        email_input.send_keys()
        password_input.send_keys()

        sign_up_button2 = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button2.click()

        time.sleep(2)

        registration_message = self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')
        registration_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert registration_message.text == "Registration failed!"
        assert registration_problem.text == "Username field required."

        registration_failed_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        registration_failed_button.click()


# ATC005 - Bejelentkezés funkció ellenőrzése üres mező kitöltéssel
    def test_login1(self):
        sing_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sing_in_page_button.click()

        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys()
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys()

        sing_in_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sing_in_button.click()

        login_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        login_problem = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-text"]')))
        assert login_message.text == "Login failed!"
        assert login_problem.text == "Email field required."

        login_failed_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        login_failed_button.click()


# ATC006 - Bejelentkezés funkció ellenőrzése helytelen adattal (jelszó)
    def test_login2(self):
        sing_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sing_in_page_button.click()
        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys(user["email"])
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys('badpassword')

        sing_in_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sing_in_button.click()

        login_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="swal-title"]')))
        login_problem = self.browser.find_element(By.XPATH, '//div[@class="swal-text"]')
        assert login_message.text == "Login failed!"
        assert login_problem.text == "Invalid user credentials."

        login_failed_button = self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
        login_failed_button.click()


# ATC007 - Bejelentkezés helyes adatokkal
    def test_login3(self):
        sign_in_page_button = self.browser.find_element(By.XPATH, '//a[@href="#/login"]')
        sign_in_page_button.click()

        email_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
        email_input.send_keys(user["email"])
        password_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
        password_input.send_keys(user["password"])

        sign_in_button = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
        sign_in_button.click()

        your_feed = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@class="nav-link router-link-exact-active active"]')))
        assert your_feed.is_displayed()


# ATC008 - Több oldalas lista bejárása (Global Feed oldalai)
    def test_page_number(self):
        login(self.browser, user["email"], user["password"])

        page_numbers_list = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]')))
        for page in page_numbers_list:
            page.click()
            actual_page = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//li[@class="page-item active"]')))
            assert page.text == actual_page.text


# ATC009 - Lista bejárás / adatok listázása (tag szűrés alapján)
    def test_tags(self):
        login(self.browser, user["email"], user["password"])

        dolor_tag = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="sidebar"]/div[@class="tag-list"]/a[@href="#/tag/dolor"]')))
        dolor_tag.click()

        article_list = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="preview-link"]/h1')))
        assert len(article_list) != 0


# ATC010 - Cikk létrehozása helytelen mező kitöltéssel (üres mezőkkel)
    def test_article_create1(self):
        login(self.browser, user["email"], user["password"])

        new_article_link = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))
        new_article_link.click()

        article_title_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
        article_about_input = self.browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
        article_main_input = self.browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
        article_tags_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
        publish_article_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title_input.send_keys()
        article_about_input.send_keys()
        article_main_input.send_keys()
        article_tags_input.send_keys()
        publish_article_button.click()

        error_message_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))
        assert error_message_button.is_displayed()
        error_message_button.click()


# ATC011 - Cikk létrehozása, új adatbevitel ellenőrzése
    def test_article_create2(self):
        login(self.browser, user["email"], user["password"])

        new_article_link = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="#/editor"]')))
        new_article_link.click()

        article_title_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
        article_about_input = self.browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
        article_main_input = self.browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
        article_tags_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
        publish_article_button = self.browser.find_element(By.XPATH, '//button[@type="submit"]')

        article_title_input.send_keys(article["title"])
        article_about_input.send_keys(article["about"])
        article_main_input.send_keys(article["main"])
        article_tags_input.send_keys(article["tags"])
        publish_article_button.click()

        new_article_title = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
        assert new_article_title.text == article["title"]

# ATC012 - Saját cikk törlésének ellenőrzése
    def test_article_delete(self):
        login(self.browser, user["email"], user["password"])

        time.sleep(5)

        create_article(self.browser, article["title"], article["about"], article["main"], article["tags"])

        time.sleep(5)

        article_url = self.browser.current_url
        delete_article_button = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_article_button.click()

        time.sleep(5)

        assert self.browser.current_url != article_url


# ATC013 - Komment hozzáadása, új adatbevitel ellenőrzése
    def test_comment_create(self):
        login(self.browser, user["email"], user["password"])

        time.sleep(5)

        create_article(self.browser, article["title"], article["about"], article["main"], article["tags"])

        comment_input = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))
        comment_input.send_keys(comment["text"])
        post_comment_button = self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
        post_comment_button.click()

        new_comment = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card"]')))[0]
        assert new_comment.is_displayed()


# ATC014 - Komment törlése funkció ellenőrzése
    def test_comment_delete(self):
        login(self.browser, user["email"], user["password"])

        time.sleep(5)

        user_article = self.browser.find_element(By.XPATH, '//a[@class="preview-link"][1]')
        user_article.click()

        time.sleep(5)

        create_comment(self.browser, comment["text"])

        delete_comment_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//i[@class="ion-trash-a"]')))
        delete_comment_button.click()

        comments = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="card"]')))
        comment_pieces = len(comments)
        assert comment_pieces != 0


# ATC015 - Cikk létrehozása / ismételt és sorozatos adatbevitel adatforrásból
    def test_import_data_from_file(self):
        login(self.browser, user["email"], user["password"])

        time.sleep(5)

        with open('C:\\Users\\kohar\\PycharmProjects\\conduit\\test_conduit_vizsgaremek\\import_data.csv', 'r') as file:
            csv_reader = csv.reader(file, delimiter=';')
            for row in csv_reader:
                create_article(self.browser, row[0], row[1], row[2], row[3])
                time.sleep(1)
                new_article_title = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h1')))
                assert new_article_title.text == row[0]


# ATC016 - Címkék kimentése az oldalról / adatok lementése a felületről csv fájlba
    def test_save_data_to_file(self):
        login(self.browser, user["email"], user["password"])

        tag_list = WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By. XPATH, '//div[@class="sidebar"]/div/a[@class="tag-pill tag-default"]')))
        with open('C:\\Users\\kohar\\PycharmProjects\\conduit\\test_conduit_vizsgaremek\\tag_list.csv', 'w') as file:
            writer = csv.writer(file)
            for tag in tag_list:
                writer.writerow([tag.text])
        with open('C:\\Users\\kohar\\PycharmProjects\\conduit\\test_conduit_vizsgaremek\\tag_list.csv', 'r') as file:
            first_row = file.readline().rstrip('\n')
            assert first_row == tag_list[0].text


# ATC017 - Kijelentkezés funkció ellenőrzése
    def test_log_out(self):
        login(self.browser, user["email"], user["password"])

        log_out_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@active-class="active"]')))
        log_out_button.click()

        sign_in_page_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="#/login"]')))
        assert sign_in_page_button.is_displayed()