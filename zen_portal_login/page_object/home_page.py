from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.base_page import BasePage


class HomePage(BasePage):



    __login_email_text_box = (By.XPATH, "//div[@class='email-input']//input[@placeholder='Enter your mail']")
    __login_password_text_box = (By.XPATH , "//input[@placeholder='Enter your password ']")
    __signin_button = (By.XPATH, "//button[@type='submit']")
    __email_field_error_message = By.XPATH , "//p[text()='*Invalid email!']"
    __password_field_error_message = By.XPATH , "//p[text() ='*Incorrect password!']"
    __login_info = (By.XPATH, "//div[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def get_web_driver_wait(self):
        return WebDriverWait(self.__driver, 10)

    def enter_email_field(self,value):
        self.enter_text(self.__login_email_text_box,value,"Email address field")

    def enter_password_field(self,value):
        self.enter_text(self.__login_password_text_box,value,"Password field")

    def click_button(self,value):
        self.click(self.__signin_button, "SignIn Button")

    def check_incorrect_email_address(self, field_name):
        try:
            error_message = self.get_web_driver_wait().until(EC.visibility_of_element_located(self.__email_field_error_message))
            return "Incorrect email address", error_message.text.strip()
        except TimeoutException:
            return False


    def check_incorrect_password_field(self,field_name):
        try:
            error_message = self.get_web_driver_wait().until(EC.visibility_of_element_located(self.__password_field_error_message))
            return "Incorrect Password", error_message.text.strip()
        except TimeoutException:
            return False

    def login_info(self):
        return self.get_text(self.__login_info, "Login header")