from app import add


def test_add():
    result = add(2, 3)
    expected = 5

    if result != expected:
        raise Exception(f"Test failed: {result} != {expected}")
