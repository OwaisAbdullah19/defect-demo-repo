from app.main import total


def test_total():
    assert total([{"price": 2}, {"price": 3}]) == 5


def test_load_items_missing_file():
    pass
