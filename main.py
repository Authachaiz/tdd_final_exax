def calculate_price(num_dozen):
    if num_dozen < 5:
        price_per_dozen = 36
    else:
        price_per_dozen = 34.992
    price = num_dozen * price_per_dozen
    return price
