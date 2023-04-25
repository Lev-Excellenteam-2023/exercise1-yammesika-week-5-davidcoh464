def get_recipe_price(prices, optionals = None, **ingredients):
    if type(prices) != dict:
        raise TypeError(prices, "is not dictionary")
    if optionals == None:
        optionals = []
    final_price = 0
    for item, price in prices.items():
        if item in ingredients and item not in optionals:
            final_price += int((ingredients[item]/100)*price)
    return final_price

print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))