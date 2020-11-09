from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth.models import User


class PruebasIntegracion(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(PruebasIntegracion, cls).setUpClass()
        cls.selenium = WebDriver()
        User.objects.create_user('test_user', password='12345678')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(PruebasIntegracion, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test_user')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('12345678')
        self.selenium.find_element_by_name('login-button').click()

    def test_signup(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/signup/'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('test_user2')
        password_input = self.selenium.find_element_by_name('password1')
        password_input.send_keys('12345678')
        password_input = self.selenium.find_element_by_name('password2')
        password_input.send_keys('12345678')
        self.selenium.find_element_by_name('signup-button').click()
