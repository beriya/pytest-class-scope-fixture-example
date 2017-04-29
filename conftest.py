import pytest


class DriverFactory:
    def __init__(self, lang="en"):
        self.__lang = lang

    def l10n(self):
        print("LANG start: ", self.__lang)
        return self.__lang

    def driver(self):
        return "SUPER DRIVER"


@pytest.fixture(scope="class", params=["ru", "en"])
def driver(request):
    print("DRIVER start")

    yield DriverFactory(request.param)

    print("DRIVER stop")


@pytest.fixture(scope="class")
def page(request, driver):
    print("PAGE start")

    print(driver.driver(), driver.l10n())

    return "SUPER PAGE"
