# receipt.py
# Week 8 - Tutorial 8: Food Delivery System - receipt module
# Responsibility: do the bill calculations and print the receipt.
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110

SERVICE_RATE = 0.05  # 5% service charge


def print_receipt(name, food, quantity, price, delivery_charges):

    subtotal = quantity * price
    # Round to sen (2 d.p.) before adding, so the printed lines always add up
    # to the printed total (e.g. RM 0.30 + RM 0.01 = RM 0.31, not RM 0.32)
    service_charge = round(subtotal * SERVICE_RATE, 2)
    grand_total = subtotal + service_charge + delivery_charges

    print("\n========== RECEIPT ==========")
    # Order details
    print(f"Customer : {name}")
    print(f"Food     : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price    : RM {price:.2f}")
    print("-----------------------------")
    # Breakdown of charges
    print(f"Subtotal : RM {subtotal:.2f}")
    print(f"Service Charge (5%) : RM {service_charge:.2f}")
    print(f"Delivery Charge : RM {delivery_charges:.2f}")
    print("-----------------------------")
    print(f"TOTAL    : RM {grand_total:.2f}")
    print("=============================")

    return grand_total
