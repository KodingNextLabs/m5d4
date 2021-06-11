
import pytest

@pytest.fixture
def get_token_jwt():
    # tester
    return 'JWT 97hfiuy3bd78wd8.duasdjkbxisada.sdnsaiuh78ugsjbuisa'


def test_login_api(get_token_jwt):
    # tesr add produc
    token = "JWT 97hfiuy3bd78wd8.duasdjkbxisada.sdnsaiuh78ugsjbuisa"
    assert get_token_jwt == token,"login gagal"