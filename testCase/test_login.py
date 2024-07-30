import pytest

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_01Login:
    baseurl = ReadConfig.getApplicationURL()
    username =ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageLoginTitle(self,setup):
        self.logger.info("********Test_01Login******")
        self.logger.info("********test_homePageLoginTitle******")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = "Your store. Login"
        exp_title = self.driver.title

        if act_title == exp_title:
            assert True
            self.logger.info("********test_homePageLoginTitle is PASSED******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageLoginTitle.png")
            assert False
            self.logger.error("********test_homePageLoginTitle is FAILED******")
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_validlogin(self,setup):
        self.logger.info("********Test_01Login******")
        self.logger.info("********test_validlogin******")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********test_validlogin is PASSED******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_validlogin.png")
            assert False
            self.logger.error("********test_validlogin is FAILED******")
            self.driver.close()


# pytest -v -s -n=2 testCase\test_login.py --browser chrome  to run paralelly
# pytest -v -s  testCase\test_login.py --browser chrome
