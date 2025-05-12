import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert isinstance(buns, list)

        for bun in buns:
            assert isinstance(bun, Bun)
            assert bun.get_price() > 0

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert isinstance(ingredients, list)

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
            assert ingredient.get_price() > 0

    @pytest.mark.parametrize("bun_name, expected_price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_bun_prices_price_matched(self, bun_name, expected_price):
        database = Database()
        buns = database.available_buns()

        bun = None
        for b in buns:
            if b.get_name() == bun_name:
                bun = b

        assert bun is not None
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_name, expected_price", [
        ("hot sauce", 100),
        ("sour cream", 200),
        ("chili sauce", 300),
        ("cutlet", 100),
        ("dinosaur", 200),
        ("sausage", 300)
    ])
    def test_ingredient_prices_price_matched(self, ingredient_name, expected_price):
        database = Database()
        ingredients = database.available_ingredients()

        ingredient = None
        for i in ingredients:
            if i.get_name() == ingredient_name:
                ingredient = i

        assert ingredient is not None
        assert ingredient.get_price() == expected_price
