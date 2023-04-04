from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def login(browser):
    sign_in_page_button = browser.find_element(By.XPATH, '//a[@href="#/login"]')
    sign_in_page_button.click()

    email_input = browser.find_element(By.XPATH, '//input[@placeholder="Email"]')
    email_input.send_keys("tesztel@gmail.com")
    password_input = browser.find_element(By.XPATH, '//input[@placeholder="Password"]')
    password_input.send_keys("Password1.")

    sign_in_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')))
    sign_in_button.click()

def create_article(browser):
    new_article_button = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
    new_article_button.click()

    article_title_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
    article_about_input = browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
    article_main_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
    article_tags_input = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
    publish_article_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    article_title_input.send_keys("Ide kerül a címe a cikknek")
    article_about_input.send_keys("Ide írjuk, hogy miről fog szólni a cikk")
    article_main_input.send_keys("Ide írjuk magának a cikknek a tartalmát")
    article_tags_input.send_keys("testtags")
    publish_article_button.click()

def create_article_data(browser, title_input, about_input, main_input, tag_input):
    new_article_button = browser.find_element(By.XPATH, '//a[@href="#/editor"]')
    new_article_button.click()

    article_title_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Article Title"]')))
    article_about_input = browser.find_element(By.XPATH, '//input[starts-with(@placeholder,"What")]')
    article_main_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write your article (in markdown)"]')
    article_tags_input = browser.find_element(By.XPATH, '//input[@placeholder="Enter tags"]')
    publish_article_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    article_title_input.send_keys(title_input)
    article_about_input.send_keys(about_input)
    article_main_input.send_keys(main_input)
    article_tags_input.send_keys(tag_input)
    publish_article_button.click()

def create_comment(browser):
    comment_input = browser.find_element(By.XPATH, '//textarea[@placeholder="Write a comment..."]')
    post_comment_button = browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')
    comment_input.send_keys("Ez egy teszt komment.")
    post_comment_button.click()