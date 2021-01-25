import pytest
import requests


@pytest.fixture
def target_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def target_status_code(request):
    return request.config.getoption("--status_code")


def test_status_code_of_entered_url(target_url, target_status_code):
    response = requests.get(target_url)
    actual_status_code = response.status_code
    assert actual_status_code == target_status_code

