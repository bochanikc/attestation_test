import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", "-B",
        action="store",
        default="chrome",
        help="choose browser"
    )

    parser.addoption(
        "--url", "-U",
        action="store",
        default="http://attestation.test/",
        help="write url"
    )


@pytest.fixture
def browser(request):
    # browser_param = request.param
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "ie":
        driver = webdriver.Ie()
    elif browser_param == "Remote":
        driver = webdriver.Remote("http://172.16.169.137:4444/",
                                  desired_capabilities={'browserName': 'chrome'})
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    driver.get(request.config.getoption("--url"))
    request.addfinalizer(driver.quit)

    return driver

