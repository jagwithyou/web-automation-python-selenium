from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.NAME, "login")     #this line means we want to find a element whose NAME is q
PASSWORD_INPUT = (By.NAME, "password")     #this line means we want to find a element whose NAME is q
SIGNIN_BUTTON = (By.NAME, "commit")

PROFILE_BUTTON = (By.XPATH, "//div[text()='Incorrect username ']")