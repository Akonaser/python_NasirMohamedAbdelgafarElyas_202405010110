# utils.py
# Tutorial 3 - Cafe Bill Calculator (logic functions)
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110

# Menu prices in RM, kept in one place so they're easy to change
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


# this is a function for reading a quantity safely
def get_quantity(prompt):
    # keep asking until the user types a whole number of 0 or more
    while True:
        try:
            quantity = int(input(prompt))
            if quantity >= 0:
                return quantity
            print("Quantity cannot be negative. Try again.")
        except ValueError:
            print("Please enter a whole number (e.g. 0, 1, 2).")


# this is a function for calculating
def calculate_total(coffee, tea, sandwich):
    # multiply each quantity by its price, then add the three subtotals
    total = (coffee * COFFEE_PRICE) + (tea * TEA_PRICE) + (sandwich * SANDWICH_PRICE)

    return total


# this is a function for printing the receipt
def print_receipt(name, coffee, tea, sandwich, total):  # name, 3 quantities and the total

    print("\n===== RECEIPT =====")

    # show who the receipt is for and how many of each item they bought
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")

    print("-------------------")
    # always show money with 2 decimal places
    print(f"Total = RM {total:.2f}")
