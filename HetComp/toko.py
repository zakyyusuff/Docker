def price_with_discount(product, discount):
    assert 0 < discount < 1, "discount expects a value between 0 and 1"
    new_price = int(product["price"] * (1 - discount))
    return new_price