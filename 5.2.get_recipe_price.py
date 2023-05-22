def get_recipe_price(prices: dict, optionals: list = None, **ingredients) -> int:
    """
    Calculates the total price of a recipe based on ingredient prices and quantities.

    Args:
        prices (dict): A dictionary mapping ingredient names to their respective prices.
        optionals (list, optional): A list of optional ingredients. Defaults to None.
        **ingredients: Keyword arguments representing ingredient names and quantities.

    Returns:
        int: The total price of the recipe.

    Raises:
        TypeError: If the prices argument is not a dictionary.

    """
    if not isinstance(prices, dict):
        raise TypeError(f"{prices} is not a dictionary")

    if optionals is None:
        optionals = []

    final_price = 0

    for item, price in prices.items():
        if item in ingredients and item not in optionals:
            final_price += int((ingredients[item] / 100) * price)

    return final_price


if __name__ == "__main__":
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({}))
