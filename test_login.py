import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in login_page.get_flash_message()
