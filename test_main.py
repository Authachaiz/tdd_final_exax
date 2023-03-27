from main import calculate_price

def test_calculate_price_when_buying_1_dozen():
    num_dozen = 1
    expected_price = 36
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_less_than_5_dozen():
    num_dozen = 3
    expected_price = 108
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_5_dozen_or_more():
    num_dozen = 5
    expected_price = 174.95999999999998
    assert calculate_price(num_dozen) == expected_price

def test_calculate_price_when_buying_10dozen():
    num_dozen = 10
    expected_price = 349.91999999999996
    assert calculate_price(num_dozen) == expected_price