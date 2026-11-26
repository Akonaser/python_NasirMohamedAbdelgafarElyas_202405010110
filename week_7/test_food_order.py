# test_food_order.py
# Week 7 - Tutorial 7: pytest tests for food_order.py
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110
#
# Run with:  pytest

# The template calls food_order(...), but the function in food_order.py is
# named calculate_total. Importing it under the name food_order fixes that.
from food_order import calculate_total as food_order


def test_order1():
    assert food_order(10, 2) == 20


# test if total food order is equal to 30
def test_order2():
    assert food_order(15, 2) == 30


# test if total food order is equal to 100
def test_order3():
    assert food_order(25, 4) == 100


# test if total food order is equal to 10
def test_order4():
    assert food_order(10, 1) == 10


# test if total food order is equal to "invalid price"
def test_invalid_price():
    assert food_order(-5, 2) == "invalid price"
    assert food_order(0, 2) == "invalid price"


# test if total food order is equal to "invalid quantity"
def test_invalid_quantity():
    assert food_order(10, 0) == "invalid quantity"
    assert food_order(10, -3) == "invalid quantity"
