from pages.login_page import LoginPage
from utilities.config_reader import get_application_url
from utilities.csv_reader import read_test_data


test_data = read_test_data("testdata/test_data.csv")


def test_invalid_login(driver):

    driver.get(get_application_url())

    login_page = LoginPage(driver)

    login_page.login(
        test_data[0]["email"],
        test_data[0]["password"]
    )

    warning_message = login_page.get_warning_message()

    assert "No match for E-Mail Address and/or Password." in warning_message