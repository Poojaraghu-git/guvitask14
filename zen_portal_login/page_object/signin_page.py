from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import logger
from page_object.base_page import BasePage


class SignInPage(BasePage):

    __welcome_content = (By.XPATH, "//p[@class='student-name']")
    __drop_down_menu = (By.XPATH, "//img[@id='profile-click-icon']")


    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def get_web_driver_wait(self):
        return WebDriverWait(self.__driver, 10)

    def welcome_message(self):
        return self.get_text(self.__welcome_content,"Welcome page details")


    def select_student_dashboard(self):
        element = self.get_web_driver_wait().until(EC.element_to_be_clickable((By.ID, "profile-click-icon")))
        element.click()
        logger.info("Clicked on student dashboard dropdown")

    def new_launch_popup(self):
        element = self.get_web_driver_wait().until(EC.visibility_of_element_located((By.XPATH, "//button[@class='custom-close-button']")))
        element.click()
        logger.info("Clicked on new launch popup")

    def click_on_log_out_button(self):
        element = self.get_web_driver_wait().until(EC.visibility_of_element_located((By.XPATH, "//div[@class='user-avatar-menu' and text()='Log out']")))
        element.click()
        logger.info("Clicked on log out button")


