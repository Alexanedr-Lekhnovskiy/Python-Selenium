import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="firefox", help='browser type')
    parser.addoption("--base_url", action='store', default='http://php4dvd', help='base URL')


@pytest.fixture(scope='module')
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='module')
def base_url(request):
    return request.config.getoption("--base_url")
