from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', help="Choose lang")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nStart chrome browser for test with '{}' language".format(user_language))
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()


