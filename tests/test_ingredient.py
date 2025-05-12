from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_price_returns_current_prince(self):
        ingredient1 = Ingredient("соус", "кетчуп", 1.99)
        ingredient2 = Ingredient("начинка", "сыр", 2.99)

        assert ingredient1.get_price() == 1.99
        assert ingredient2.get_price() == 2.99

    def test_get_name_returns_current_name(self):
        ingredient1 = Ingredient("соус", "кетчуп", 1.99)
        ingredient2 = Ingredient("начинка", "сыр", 2.99)

        assert ingredient1.get_name() == "кетчуп"
        assert ingredient2.get_name() == "сыр"

    def test_get_type_return_current_type(self):
        ingredient1 = Ingredient("соус", "кетчуп", 1.99)
        ingredient2 = Ingredient("начинка", "сыр", 2.99)

        assert ingredient1.get_type() == "соус"
        assert ingredient2.get_type() == "начинка"

    def test_create_ingredient_successful_creation(self):
        new_ingredient = Ingredient("filling", "ham", 3.99)

        assert new_ingredient.get_type() == "filling"
        assert new_ingredient.get_name() == "ham"
        assert new_ingredient.get_price() == 3.99
