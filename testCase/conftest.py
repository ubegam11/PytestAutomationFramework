import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching firefox")
    elif browser=='edge':
        driver=webdriver.Edge()
        print("Launching Edge")
    else:
        driver=webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

###################Pytest HTML Report#######################
# It is hook for adding envirnment info to the HTML report

# def pytest_configuration(config):
#     config._metadata['Project Name']='nop commerce'
#     config._metadata['Module Name']='Customer'
#     config._metadata['Tester']='ubegam'

# It ishook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
