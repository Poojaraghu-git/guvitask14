from conftest import logger
from page_object import signin_page
from page_object.home_page import HomePage
from page_object.signin_page import SignInPage


class test_successful_login:

    def test_user_is_able_to_login_successfully(self,driver):
        home_page = HomePage(driver)
        home_page.enter_email_field("poojaraghuraman.297@gmail.com")
        home_page.enter_password_field("1@Vegetass")
        home_page.click_button("signin")
        signin_page = SignInPage(driver)
        signin_page.new_launch_popup()
        assert "Welcome, " in signin_page.welcome_message(), "Welcome message did not appear"

    def test_login_unsuccessful(self,driver):
        home_page = HomePage(driver)
        home_page.enter_email_field("poojaraghuraman.2979@gmail.com")
        home_page.enter_password_field("1@Vegetass")
        home_page.click_button("signin")

        if home_page.check_incorrect_email_address("email"):
            logger.info("Invalid Email Address")
            assert True
        elif home_page.check_incorrect_password_field("password"):
            logger.info("Invalid Password")
            assert True
        else:
            logger.info("No error message")


    def test_log_out_functionality(self,driver):
        home_page = HomePage(driver)
        home_page.enter_email_field("poojaraghuraman.297@gmail.com")
        home_page.enter_password_field("1@Vegetass")
        home_page.click_button("signin")
        signin_page = SignInPage(driver)
        signin_page.new_launch_popup()
        signin_page.select_student_dashboard()
        signin_page.click_on_log_out_button()
        assert "Login" in home_page.login_info() , "Login page did not load"
        driver.quit()

