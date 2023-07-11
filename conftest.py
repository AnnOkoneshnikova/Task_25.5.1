from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def set():
   driver = webdriver.Chrome('/Users/annokoneshnikova/webdriver/chromedriver_107')
   driver.get('http://petfriends.skillfactory.ru/login')

   yield

   driver.quit()
