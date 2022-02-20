from tests import BaseClass
from locator.github_login_page_locator import *
from selenium.webdriver.common.keys import Keys

class TestGithubPage(BaseClass):
    def test_1_login_wrong_username_wrong_password(self):
        ''' This is a test case to test the Github Login Page Bad case page. '''
        #Instantiating the logger
        self.log().info("Github Login Page Bad case Test Started")
        # Opening github Url
        self.driver.get("https://github.com/login")
        #accessing the username and password field and sending text to that
        self.get_element(USERNAME_INPUT).send_keys('Test') #wrong Username
        self.get_element(PASSWORD_INPUT).send_keys('test123') #Wrong Password
        #accessing the submit button and clicking it
        self.get_element(SIGNIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        #Assert
        assert self.get_element(SIGNIN_BUTTON).is_displayed()

    def test_2_login(self):
        ''' This is a test case to test the Github Login Page Good case page. '''
        #Instantiating the logger
        self.log().info("Github Login Page Good case Test Started")
        #accessing the username and password field and sending text to that
        self.get_element(USERNAME_INPUT).clear()
        self.get_element(PASSWORD_INPUT).clear()
        self.get_element(USERNAME_INPUT).send_keys('jagwithyou') #right Username
        self.get_element(PASSWORD_INPUT).send_keys('Jag143NBS@#') #right Password
        #accessing the submit button and clicking it
        self.get_element(SIGNIN_BUTTON).submit()
        #logging the test success
        self.log().info("Test Success")
        # assert self.get_element(PROFILE_BUTTON).is_displayed()


