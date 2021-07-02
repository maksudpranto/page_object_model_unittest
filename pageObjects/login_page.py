class LoginTest:
    # Identifying the Locators Here
    email_text_box_ID = "Email"
    password_text_box_ID = "Password"
    login_button_xpath = "//button[contains(text(),'Log in')]"
    logout_button_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    # Set Email
    def set_email(self, email):
        self.driver.find_element_by_id(self.email_text_box_ID).clear()
        self.driver.find_element_by_id(self.email_text_box_ID).send_keys(email)

    # Set Password
    def set_password(self, password):
        self.driver.find_element_by_id(self.password_text_box_ID).clear()
        self.driver.find_element_by_id(self.password_text_box_ID).send_keys(password)

    # Login Button Click
    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    # Log Out Button Click
    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
