import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    return Mock(spec=Bun)


@pytest.fixture
def bun(mock_bun):
    mock_bun.get_name.return_value = "Тестовая булочка"
    mock_bun.get_price.return_value = 2.0
    return mock_bun


@pytest.fixture
def ingredient():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = "Тестовый ингредиент"
    mock_ingredient.get_price.return_value = 0.5
    mock_ingredient.get_type.return_value = "Тестовый тип"
    return mock_ingredient


@pytest.fixture
def mock_ingredient():
    return Mock(spec=Ingredient)
