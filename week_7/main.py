# main.py
# Week 7 - Tutorial 7: FoodExpress ordering system (fixed version)
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110
#
# Run with:  python main.py
# See W7_documentation.txt for the list of bugs found and how they were fixed.

from food_order import calculate_total


def read_number(prompt, convert):
    # Keep asking until the input can be converted (float or int).
    # Without this, typing "abc" would crash the program with a ValueError.
    while True:
        try:
            return convert(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        price = read_number("Price (RM): ", float)
        quantity = read_number("Quantity: ", int)

        # Use the validated logic in food_order.py instead of price * quantity here
        total = calculate_total(price, quantity)

        # calculate_total returns a message (str) when the order is invalid
        if isinstance(total, str):
            print(f"Order rejected: {total}. Please try again.\n")
            continue

        print(f"Total Payment = RM {total:.2f}")
        break


if __name__ == "__main__":
    main()
