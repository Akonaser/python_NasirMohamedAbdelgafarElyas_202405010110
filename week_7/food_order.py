# food_order.py
# Week 7 - Tutorial 7: FoodExpress order logic
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110


def calculate_total(price, quantity):
    # Validate the price first: an item can't be free or cost a negative amount
    if price <= 0:
        return "invalid price"

    # Validate the quantity: you must order at least 1 item
    if quantity <= 0:
        return "invalid quantity"

    # Both values are valid, so the total is price x quantity
    return price * quantity
