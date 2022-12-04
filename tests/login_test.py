import selenium
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
#from selenium.webdriver.common.by import By

class TestLogin():

    @pytest.fixture(scope="class")

    def test_setup(self):
        global driver
        driver = selenium.webdriver.Chrome(executable_path= "C://Users//RAMASWAMI//PycharmProjects//End to End Automation//drivers//chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        print("Test completed")
        driver.close()
        driver.quit()

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    #    driver.find_element(By.NAME, "username").send_keys("Admin")
    #   driver.find_element(By.NAME, "password").send_keys("admin123")
    #  driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()



       # driver.find_element(By.CLASS_NAME, "oxd-userdropdown-img").click()
       # driver.find_element(By.LINK_TEXT, "Logout").click()

