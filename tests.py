import pytest
import requests

def test_foo():
    r = requests.get('https://github.com/mjordan')
    assert r.status_code == 200
