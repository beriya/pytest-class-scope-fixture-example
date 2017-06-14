import pytest
from itertools import product


def pytest_addoption(parser):
    """Add some command line options."""
    parser.addoption(
        "--browser",
        action="append",
        default=[],
        help="List of browsers: firefox, chrome, edge, ie")
    parser.addoption(
        "--lang", action="append", default=["en"], help="List of languages")


def pytest_generate_tests(metafunc):
    """Add multilang support."""
    if 'driver' in metafunc.fixturenames:
        langs = metafunc.config.option.lang
        browsers = metafunc.config.option.browser
        argvals = list(product(langs, browsers))
        idfns = []
        for val in argvals:
            idfns.append("{} - {}".format(val[0], val[1]))
        metafunc.parametrize(
            "driver", argvals, indirect=True, ids=idfns, scope="class")


class DriverFactory:
    def __init__(self, lang="en"):
        self.__lang = lang

    def l10n(self):
        print("LANG start: ", self.__lang)
        return self.__lang

    def driver(self):
        return "SUPER DRIVER"


@pytest.fixture(scope="class")
def driver(request):
    print("DRIVER start")

    print(request.param)

    yield DriverFactory(request.param)

    print("DRIVER stop")


@pytest.fixture(scope="class")
def page(driver):
    print("PAGE start")

    # print(driver.driver(), driver.l10n())

    return "SUPER PAGE"
