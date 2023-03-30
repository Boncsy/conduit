from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)
URL = "http://localhost:1667/"
browser.get(URL)
browser.maximize_window()

# Regisztráció helytelen jelszóval

sign_up_button = browser.find_element(By.LINK_TEXT, 'Sign up')
sign_up_button.click()

username_input = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

username_input.send_keys('TeszterBéla')
email_input.send_keys('teszt@gmail.com')
password_input.send_keys('rossz')

sign_up_button2 = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_up_button2.click()

time.sleep(2)

registration_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
registration_problem = browser.find_element(By.XPATH, '//div[@class="swal-text"]')
assert registration_message.text == "Registration failed!"
assert registration_problem.text == "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter."

registration_failed_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
registration_failed_button.click()

# Regisztráció üres mezővel
username_input = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

username_input.send_keys()
email_input.send_keys()
password_input.send_keys()

sign_up_button2 = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_up_button2.click()

time.sleep(2)

registration_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
registration_problem = browser.find_element(By.XPATH, '//div[@class="swal-text"]')
assert registration_message.text == "Registration failed!"
assert registration_problem.text == "Username field required."

registration_failed_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
registration_failed_button.click()

''''# Regisztráció helyes adatokkal
username_input = browser.find_element(By.XPATH, '//input[@placeholder="Username"]')
email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

username_input.send_keys('TeszterBéla')
email_input.send_keys('teszt@gmail.com')
password_input.send_keys('Password8.')

sign_up_button2 = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_up_button2.click()

time.sleep(2)

registration_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
registration_problem = browser.find_element(By.XPATH, '//div[@class="swal-text"]')
assert registration_message.text == "Welcome!"
assert registration_problem.text == "Your registration was successful!"

registration_ok_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
registration_ok_button.click()

time.sleep(2)

user_profile = browser.find_elements(By.XPATH, '//a[@class="nav-link"]')[2]
assert user_profile.text == "Tesztiiii"' '''

# Bejelentkezés funkció ellenőrzése üres mező kitöltéssel

sing_in_page_button = browser.find_element(By.XPATH, '//a[@href="#/login"]')
sing_in_page_button.click()

email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
email_input.send_keys()
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
password_input.send_keys()

sing_in_button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sing_in_button.click()

time.sleep(2)

login_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
login_problem = browser.find_element(By.XPATH, '//div[@class="swal-text"]')
assert login_message.text == "Login failed!"
assert login_problem.text == "Email field required."

login_failed_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
login_failed_button.click()

# Bejelentkezés funkció ellenőrzése helytelen adattal (jelszó)

email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
email_input.send_keys('enedykrpbkfgibsqvj@tmmbt.com')
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
password_input.send_keys('badpassword')

sing_in_button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sing_in_button.click()

time.sleep(2)

login_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
login_problem = browser.find_element(By.XPATH, '//div[@class="swal-text"]')
assert login_message.text == "Login failed!"
assert login_problem.text == "Invalid user credentials."

login_failed_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
login_failed_button.click()

# Bejelentkezés funkció ellenőrzése helyes adatokkal

sign_in_page_button = browser.find_element(By.XPATH, '//a[@href="#/login"]')
sign_in_page_button.click()

email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
email_input.clear()
email_input.send_keys('enedykrpbkfgibsqvj@tmmbt.com')
password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
password_input.clear()
password_input.send_keys('Password1.')

sign_in_button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
sign_in_button.click()

time.sleep(2)

user_profile = browser.find_elements(By.XPATH, '//a[@class="nav-link"]')[2]
assert user_profile.text == 'Enedyk'

# Több oldalas lista bejárás (oldalak)

page_numbers_list = browser.find_elements(By.XPATH, '//a[@class="page-link"]')
for page in page_numbers_list:
    page.click()
    time.sleep(1)
    actual_page = browser.find_element(By.XPATH, '//li[@class="page-item active"]')
    assert page.text == actual_page.text

# Lista bejárás / adatok listázása (tag szűrés alapján)

dolor_tag = browser.find_element(By.XPATH, '//div[@class="sidebar"]/div[@class="tag-list"]/a[@href="#/tag/dolor"]')
dolor_tag.click()

time.sleep(2)

article_list = browser.find_elements(By.XPATH, '//a[@class="preview-link"]/h1')
assert len(article_list) != 0


# Cikk létrehozása helytelen mező kitöltéssel (üres mezőkkel)

new_article_link = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
new_article_link.click()

time.sleep(2)

article_title_input = browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
article_about_input = browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
article_main_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
article_tags_input = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
publish_article_button = browser.find_element(By.XPATH, '//button[@type="submit"]')

article_title_input.send_keys()
article_about_input.send_keys()
article_main_input.send_keys()
article_tags_input.send_keys()
publish_article_button.click()

time.sleep(2)

error_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
assert error_message.text == 'Oops!'
error_message_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
error_message_button.click()


# Cikk létrehozása helyes adatokkal

new_article_link = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
new_article_link.click()

time.sleep(2)

article_title_input = browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
article_about_input = browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
article_main_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
article_tags_input = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
publish_article_button = browser.find_element(By.XPATH, '//button[@type="submit"]')

article_title_input.send_keys('Ide kerül a címe a cikknek.')
article_about_input.send_keys('Ide írjuk, hogy miről fog szólni a cikk')
article_main_input.send_keys('Ide írjuk magának a cikknek a tartalmát.')
article_tags_input.send_keys('testtags')
publish_article_button.click()

time.sleep(2)

new_article_title = browser.find_element(By.XPATH, '//h1')
assert new_article_title.text == 'Ide kerül a címe a cikknek.'

# Komment írás és törlése

comment_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write a comment..."]')
comment_input.send_keys('Ez egy teszt komment.')
post_comment_button = browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
post_comment_button.click()

time.sleep(2)

new_comment = browser.find_elements(By.XPATH, '//div[@class="card"]')[0]
assert new_comment.is_displayed()

comments_before = browser.find_elements(By.XPATH, '//div[@class="card"]')
comment_pieces_before = len(comments_before)

delete_button = browser.find_element(By.XPATH, '//i[@class="ion-trash-a"]')
delete_button.click()

time.sleep(2)

comments_after = browser.find_elements(By.XPATH, '//div[@class="card"]')
comment_pieces_after = len(comments_after)
assert comment_pieces_before != comment_pieces_after


# Saját cikk törlése

new_article_link = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
new_article_link.click()

time.sleep(2)

article_title_input = browser.find_element(By.XPATH, '//input[@placeholder="Article Title"]')
article_about_input = browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
article_main_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
article_tags_input = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
publish_article_button = browser.find_element(By.XPATH, '//button[@type="submit"]')

article_title_input.send_keys('Ide kerül a címe a cikknek.')
article_about_input.send_keys('Ide írjuk, hogy miről fog szólni a cikk')
article_main_input.send_keys('Ide írjuk magának a cikknek a tartalmát.')
article_tags_input.send_keys('testtags')
publish_article_button.click()

time.sleep(2)

new_article_title = browser.find_element(By.XPATH, '//h1')
assert new_article_title.text == 'Ide kerül a címe a cikknek.'

article_url = browser.current_url
delete_article_button = browser.find_element(By.XPATH, '//i[@class="ion-trash-a"]')
delete_article_button.click()

time.sleep(2)

assert browser.current_url != article_url


# Profil szerkesztése

settings_menu = browser.find_element(By.XPATH, '//a[@href="#/settings"]')
settings_menu.click()

time.sleep(2)

image_input = browser.find_element(By.XPATH, '//input[@placeholder="URL of profile picture"]')
image_input.clear()
image_input.send_keys("https://cdn-icons-png.flaticon.com/512/3480/3480315.png")

update_button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')
update_button.click()

time.sleep(2)

result_message = browser.find_element(By.XPATH, '//div[@class="swal-title"]')
assert result_message.text == "Update successful!"
confirm_button = browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')
confirm_button.click()



# Kijelentkezés funkció ellenőrzése

log_out_button = browser.find_element(By.XPATH, '//a[@active-class="active"]')
log_out_button.click()

time.sleep(2)

sign_in_page_button = browser.find_element(By.XPATH, '//a[@href="#/login"]')
assert sign_in_page_button.is_displayed()



browser.quit()