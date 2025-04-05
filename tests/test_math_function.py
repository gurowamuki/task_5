import pytest
from src.math_functions import add

@pytest.fixture
def sample_data():
    return [(2, 3, 5), (-1, 1, 0), (10, 20, 30)]

def test_add(sample_data):
    for a, b, expected in sample_data:
        assert add(a, b) == expected