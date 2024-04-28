from selenium.webdriver.common.by import By
#from TestCases.conftest import

class HomePage:
    def __init__(self,driver):
        self.driver= driver
    shop=[By.CSS_SELECTOR, "a[href*='shop']"]
    #find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
    name=[By.CSS_SELECTOR, "input[name='name']"]
    #self.driver.find_element(By.NAME, "email").send_keys("hinafatima@gmail.com")
    email=[By.NAME, "email"]
    #self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("qwerty34")
    password=[By.ID, "exampleInputPassword1"]
    #self.driver.find_element(By.ID, "exampleCheck1").click()
    check=[By.ID, "exampleCheck1"]
    def ShopItems(self):
        #self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']")
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getpassword(self):
        return self.driver.find_element(*HomePage.password)
    def getCheck(self):
        return self.driver.find_element(*HomePage.check)

  