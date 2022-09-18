import time

from selenium.webdriver.common.by import By


class LoginPage:
    username_input_text_id = "username"
    password_input_text_id = "password"
    login_btn_link_text = "Login"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.username_input_text_id).click()
        self.driver.find_element(By.ID, self.username_input_text_id).send_keys(username)
        time.sleep(1)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.password_input_text_id).click()
        self.driver.find_element(By.ID, self.password_input_text_id).send_keys(password)
        time.sleep(1)

    def click_login_button(self):
        self.driver.find_element(By.LINK_TEXT, self.login_btn_link_text).click()
        time.sleep(1)

    # # method for test_login
    # def login_method(self, username, password):
    #     self.set_username(username)
    #     self.set_username(password)
    #     self.click_login_button()

    def login_method(self, username, password):
        self.driver.find_element(By.ID, self.username_input_text_id).click()
        self.driver.find_element(By.ID, self.username_input_text_id).send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.ID, self.password_input_text_id).click()
        self.driver.find_element(By.ID, self.password_input_text_id).send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, self.login_btn_link_text).click()
        time.sleep(1)
