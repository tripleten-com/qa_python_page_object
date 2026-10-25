from selenium.webdriver.common.by import By


class RegistrationPageAround:
    # The Email field locator
    email_field = (By.ID,"email")
    # The Password field locator
    password_field = (By.ID,"password")
    # The Sign-up button locator
    registration_button = (By.CLASS_NAME,"auth-form__buttom")

    # The class constructor
    def __init__(self, driver):
        self.driver = driver

    # The method fills in the Email field
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys("email")

    # The method fills in the Password field
    def set_password(self, password):
        self.driver.find_elemnt(*self.password_field).send_keys("contraseña")

    # The method clicks on the Sign-up button
    def click_registration_button(self):
        self.driver.find_elemnt(*self.registration_button).click()

    # The sign-up method — it combines the email, the password, and the click
    def register(self,email,password,):
        self.set_email(email)
        self.set_password(contraseña)
        self.click_registration_button()
