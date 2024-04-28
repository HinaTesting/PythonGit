import time

import pytest

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilitites.BaseClass import BaseClass
from selenium.webdriver.common.by import By

@pytest.mark.usefixture("setup")
class TestHomePage(BaseClass):
    def test_formSubmission(self,setup,getData):
        log = self.getLogger()
                # ID,Xpath, CSSSelector, Classname,name,linktext
        #self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
        self.driver.implicitly_wait(4)
        homepage=HomePage(self.driver)
        log.info("Firstname is"+getData["Firstname"])
        homepage.getName().send_keys(getData["Firstname"])
        #self.driver.find_element(By.NAME, "email").send_keys("hinafatima@gmail.com")
        #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("qwerty34")
        #self.driver.find_element(By.ID, "exampleCheck1").click()
        homepage.getEmail().send_keys(getData["Lastname"])
        homepage.getpassword().send_keys("qwerty34")
        homepage.getCheck().click()

        # CSS- tagname[attribute='value']->input[type='submit'], #id,.classname
        # XPath- //tagname[@attribute='value']->//input[@type='submit']

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(5)
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message
        self.driver.get_screenshot_as_file("Screen1.png")
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.test_HomepageData)
    def getData(self,request):
        return request.param

