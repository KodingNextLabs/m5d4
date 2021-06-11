import pytest

@pytest.mark.shaufi
def test_file2_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


@pytest.mark.yanwar
def test_file2_method2():
    a = "shaufi"
    b = "agung"
    assert a == b, "test failed"