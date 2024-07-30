import pytest

from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtil
class Test_01Login_ddt:
    baseurl = ReadConfig.getApplicationURL()
    path=".//TestData/userData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********Test_01Login******")
        self.logger.info("********test_validlogin******")

        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)

        self.rows=XLUtil.getRowCount(self.path,'Sheet2')
        list_status=[]
        for r in range(2,self.rows+1):
            self.username=XLUtil.readData(self.path,'Sheet2',r,1)
            self.password=XLUtil.readData(self.path,'Sheet2',r,2)
            self.exp=XLUtil.readData(self.path,'Sheet2',r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp=="Pass":
                    self.logger.info("******** PASSED******")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.error("******** FAILED******")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp=="Pass":
                    self.logger.info("******** fail******")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.error("******** Pass******")
                    self.lp.clickLogout()
                    list_status.append("Pass")

        print(list_status)

# pytest -v -s -n=2 testCase\test_login.py --browser chrome  to run paralelly
# pytest -v -s  testCase\test_login.py --browser chrome
