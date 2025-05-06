import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name, price, expected_name, expected_price",
        [
            ("Классическая булочка", 0.99, "Классическая булочка", 0.99),
            ("Шоколадная булочка", 2.49, "Шоколадная булочка", 2.49),
            ("Булочка с корицей", 1.49, "Булочка с корицей", 1.49),
        ]
    )
    def test_get_name_and_price_with_various_inputs_correct_output(self, name, price, expected_name, expected_price):
        bun = Bun(name, price)

        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_get_name_returns_self_name(self):
        bun = Bun("Булочка с кунжутом", 2.0)

        assert bun.get_name() == "Булочка с кунжутом"

    def test_get_price_returns_self_price(self):
        bun = Bun("Булочка с кунжутом", 2.0)

        assert bun.get_price() == 2.0
