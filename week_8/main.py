# main.py
# Week 8 - Tutorial 8: Food Delivery System - main application module
# Responsibility: connect the modules together and run the program.
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110
#
# Run with:  python main.py

from customer import get_customer
from receipt import print_receipt


def main():

    name, food, quantity, price, delivery_charges = get_customer()  # getting the customer data

    print_receipt(name, food, quantity, price, delivery_charges)  # to print out the food receipt


if __name__ == "__main__":
    main()
