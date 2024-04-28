import time

import pytest

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilitites.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
@pytest.mark.usefixture("setup")
class TestOne(BaseClass):
    def test_e2e(self,setup):
        log=self.getLogger()
        #service_obj = Service("C:/Users/hinan/Desktop/Rahul shetty academy python selenium/chromedriver.exe")
        #driver = webdriver.Chrome(service=service_obj)
        self.driver.implicitly_wait(4)
        #driver.maximize_window()
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #  //a[contains(@href,'shop')]    a[href*='shop']
        #self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        homePage=HomePage(self.driver)
        homePage.ShopItems().click()
        log.info("getting all the card titles")

        print("getting all the card titles2")
        print("getting all the card titles3")

        print("getting all the card titles5")
        print("getting all the card titles6")
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        checkoutPage= CheckOutPage(self.driver)
        cards=checkoutPage.ShopProducts()

        for product in cards:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            #productName=checkoutPage.CardFooter().text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutPage.getCheckoutButton().click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(10)
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText
        log.info("text received ")
        log.info(successText)
        self.driver.get_screenshot_as_file("Screen2.png")




