# food_order.py
# Week 7 - Tutorial 7: FoodExpress order logic
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110

import math


def calculate_total(price, quantity):
    # Validate the price first: it must be a real, finite amount greater than 0.
    # math.isfinite() rejects float("nan") and float("inf"), which float() accepts
    # from text like "nan" or "inf" and which would otherwise print "RM nan".
    if not math.isfinite(price) or price <= 0:
        return "invalid price"

    # Validate the quantity: you must order at least 1 item
    if quantity <= 0:
        return "invalid quantity"

    # Both values are valid, so the total is price x quantity
    return price * quantity
