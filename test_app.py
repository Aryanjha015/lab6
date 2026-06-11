from app import add

def test_add():
    cases = [(2, 3, 5), (-1, -1, -2), (0, 5, 5), (-1, 1, 0)]
    for a, b, expected in cases:
        assert add(a, b) == expected
        assert isinstance(add(a, b), int)
