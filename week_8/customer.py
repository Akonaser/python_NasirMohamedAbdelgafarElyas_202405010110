# customer.py
# Week 8 - Tutorial 8: Food Delivery System - customer module
# Responsibility: collect and validate the customer's order details.
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110

DELIVERY_FEE = 5.00
MENU = ("Cake", "Muffin")


def get_customer():

    print("=== Customer Information ===")

    # Input: customer name and order details (each one checked before moving on)
    name = input("Customer Name : ").strip()

    food = input("Food Ordered (Cake/Muffin) : ").strip().capitalize()
    while food not in MENU:
        print("Sorry, we only have Cake or Muffin.")
        food = input("Food Ordered (Cake/Muffin) : ").strip().capitalize()

    quantity = read_positive("Quantity : ", int)
    price = read_positive("Price per Item (RM): ", float)

    delivery = input("Delivery (Y/N): ").strip().upper()
    while delivery not in ("Y", "N"):
        print("Please enter Y or N.")
        delivery = input("Delivery (Y/N): ").strip().upper()

    # If-else: delivery costs RM 5.00, self pick-up is free
    if delivery == "Y":
        delivery_charges = DELIVERY_FEE
    else:
        delivery_charges = 0.00

    return name, food, quantity, price, delivery_charges


def read_positive(prompt, convert):
    # Keep asking until the user enters a number greater than 0.
    # convert is int (for quantity) or float (for price).
    while True:
        try:
            value = convert(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
