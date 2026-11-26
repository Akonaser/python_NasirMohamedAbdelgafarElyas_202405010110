# main.py
# Tutorial 3 - Cafe Bill Calculator (main program)
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110
#
# Run with:  python main.py

from utils import get_quantity, calculate_total, print_receipt


def main():
    # 1. Input: customer name and how many of each item they ordered
    name = input("Customer name: ").strip()
    while name == "":
        print("Name cannot be empty.")
        name = input("Customer name: ").strip()
    while True:
        coffee = get_quantity("Coffee quantity: ")
        tea = get_quantity("Tea quantity: ")
        sandwich = get_quantity("Sandwich quantity: ")
        # an order must contain at least one item
        if coffee + tea + sandwich > 0:
            break
        print("The order is empty. Please order at least one item.")

    # 2. Process: work out the bill using the logic in utils.py
    total = calculate_total(coffee, tea, sandwich)

    # 3. Output: print the receipt
    print_receipt(name, coffee, tea, sandwich, total)


# only run main() when this file is run directly, not when it's imported
if __name__ == "__main__":
    main()
