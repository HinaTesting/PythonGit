import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope='class')
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        service_obj = Service("C:/Users/hinan/Desktop/Rahul shetty academy python selenium/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name=="firefox":
        service_obj = Service("C:/Users/hinan/Desktop/Rahul shetty academy python selenium/geckodriver-v0.34.0-win64.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "MicrosoftEdge":
        service_obj = Service("C:/Users/hinan/Desktop/Rahul shetty academy python selenium/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

#@pytest.fixture()
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )
