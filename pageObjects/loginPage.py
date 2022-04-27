from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.signin_section_id = "nav-link-accountList-nav-line-1"
        self.email_textbox_id="ap_email"
        self.email_submit_css="span #continue"

    def test_signin_section(self):
        self.driver.find_element(By.ID, self.signin_section_id).click()

    def test_email_textbox(self,mobile):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(mobile)

    def test_email_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, self.email_submit_css).click()

