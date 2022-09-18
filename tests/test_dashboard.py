import time

import allure
import pytest

from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Dashboard:

    test_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    # test_url = "https://wlsandbox.remotecoach.fit/admin/login"
    # email = "test_agent@test.com"
    # password = "Bg%1@cb9KV05"

    @allure.severity(allure.severity_level.BLOCKER)
    def test_page_verification(self, setup):
        page_title_expected = "Admin Login"
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.test_url)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == page_title_expected:
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_page_verification.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_verification_for_valid_credential(self, setup):
        page_title_expected = "Dashboard"
        print("test : Login Verification for valid credential ")
        self.driver = setup
        self.driver.get(self.test_url)
        self.loginDriver = LoginPage(self.driver)
        self.loginDriver.set_username(self.email)
        self.loginDriver.set_password(self.password)
        self.loginDriver.click_login_button()
        actual_page_title = self.driver.title
        if actual_page_title == page_title_expected:
            self.logger.info("**** test_login_verification_for_valid_credential : passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** test_login_verification_for_valid_credential :  failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_verification_for_valid_credential.png")
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_total_subscriber(self, setup):
        self.driver = setup
        self.driver.get(self.test_url)
        self.loginDriver = LoginPage(self.driver)
        self.loginDriver.login_method(self.email, self.password)
        time.sleep(3)
        self.logger.info("************* Login successful **********")
        self.logger.info("******* Navigating to Subscriber **********")

        self.dashboardDriver = DashboardPage(self.driver)
        total_subscriber = self.dashboardDriver.get_total_subscriber()
        total_subscriber = int(total_subscriber)

        if total_subscriber > 0:
            print(total_subscriber)
            self.logger.info("**** test_total_subscriber :  Passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home test_total_subscriber : Failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_total_subscriber.png")
            self.driver.close()
            assert False
