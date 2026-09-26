from selenium.webdriver.common.by import By
from utilities.logger import get_logger


class LoginPage:

    MY_ACCOUNT = (By.XPATH, "//span[text()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(__name__)

    def open_login_page(self):
        self.logger.info("Opening login page")
        self.driver.find_element(*self.MY_ACCOUNT).click()
        self.driver.find_element(*self.LOGIN_LINK).click()

    def enter_email(self, email):
        self.logger.info("Entering email")
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, email, password):
        self.open_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_warning_message(self):
        return self.driver.find_element(*self.WARNING_MESSAGE).text