from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_the_ingredient_added_to_list(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_valid_index_ingredient_remove_from_list(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_valid_indices_ingredient_moved_to_new_position(self, ingredient):
        burger = Burger()
        ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ingredient2, ingredient]

    def test_get_price_returns_correct_total_price(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 4.5

    def test_get_receipt_returns_correct_receipt(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = (
            "(==== Тестовая булочка ====)\n"
            "= тестовый тип Тестовый ингредиент =\n"
            "(==== Тестовая булочка ====)\n\n"
            "Price: 4.5"
        )
        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt
