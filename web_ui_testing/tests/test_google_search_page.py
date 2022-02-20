from tests import BaseClass
from locator.google_homepage_locator import *
from selenium.webdriver.common.keys import Keys

class TestGooglePage(BaseClass):
    def test_1_search(self):
        ''' This is a test case to test the Google Search Page page. '''
        #Instantiating the logger
        self.log().info("Google Search Page Test Started")
        #accessing the search field and sending text to that
        self.get_element(SEARCH_BAR).send_keys('Automation Testing Python Selenium')
        self.get_element(SEARCH_BAR).send_keys(Keys.RETURN)
        #logging the test success
        self.log().info("Test Success")
        assert True

