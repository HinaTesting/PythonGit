from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver= driver

    #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    products=[By.XPATH, "//div[@class='card h-100']"]
    #product.find_element(By.XPATH, "div/h4/a")
    CardFooter=[By.XPATH, "div/h4/a"]
    #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    CheckOutButton=[By.CSS_SELECTOR, "a[class*='btn-primary']"]
    def ShopProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.CardFooter)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.CheckOutButton)

