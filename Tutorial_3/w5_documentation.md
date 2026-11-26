# Tutorial 3 – Café Bill Calculator

**Name:** Nasir Mohamed Abdelgafar Elyas
**Student ID:** 202405010110

## Scenario

A small café sells three items:

| Item | Price (RM) |
|---|---:|
| Coffee | 8.50 |
| Tea | 6.00 |
| Sandwich | 12.00 |

Right now the cashier works out every bill by hand. The task is a Python program that calculates the customer's bill automatically.

---

## 1. Answer the Questions

### 1.1 Problem Statement

The café cashier calculates bills by hand, which is slow and easy to get wrong. The café needs a program that takes the customer's name and how many coffees, teas and sandwiches they ordered, then calculates the total and prints a clear receipt.

### 1.2 Inputs

| Input | Type | Example |
|---|---|---|
| Customer name | string | `Bobby` |
| Coffee quantity | integer | `3` |
| Tea quantity | integer | `3` |
| Sandwich quantity | integer | `2` |

The item prices are fixed values in the program (constants), so the user doesn't type them in.

### 1.3 Outputs

A receipt showing:

- the customer's name
- the quantity of each item
- the **total bill in RM**, to 2 decimal places

```
===== RECEIPT =====
Customer : Bobby
Coffee   : 3
Tea      : 3
Sandwich : 2
-------------------
Total = RM 67.50
```

### 1.4 Typical Process Flow

1. **Start**
2. Ask for the customer's name.
3. Ask for the quantity of coffee, tea and sandwich.
4. Multiply each quantity by its price to get each item's subtotal.
5. Add the three subtotals to get the total.
6. Print the receipt.
7. **End**

```
Input (name, quantities) -> Calculate total -> Print receipt
```

### 1.5 Constraints

- Prices are fixed: Coffee RM 8.50, Tea RM 6.00, Sandwich RM 12.00.
- Quantities must be **whole numbers** (you can't buy 1.5 coffees).
- Quantities can't be **negative**. Zero is allowed, for items the customer didn't order.
- Money is shown with **2 decimal places** (RM 67.50, not RM 67.5).
- Only the three menu items can be ordered.
- The logic functions must be in `utils.py`, and the program must run from `main.py`.

---

## 2. Decomposing the Problem

The big problem, "calculate a customer's bill", breaks into small tasks, each with one job:

| Task | What it does | Where it lives |
|---|---|---|
| **Get input** | Reads the name and the three quantities, rejecting bad values | `get_quantity()` in `utils.py`, called from `main.py` |
| **Calculate** | Works out `quantity × price` for each item and adds them up | `calculate_total()` in `utils.py` |
| **Display** | Prints the receipt in the required format | `print_receipt()` in `utils.py` |
| **Control the flow** | Calls the tasks above in order: input, then calculate, then print | `main()` in `main.py` |

Splitting it up this way means each piece can be tested and fixed on its own. For example, if a price changes, only the constant at the top of `utils.py` needs updating.

---

## 3. Pseudocode

```
CONSTANTS
    COFFEE_PRICE   = 8.50
    TEA_PRICE      = 6.00
    SANDWICH_PRICE = 12.00

FUNCTION calculate_total(coffee, tea, sandwich)
    total = coffee * COFFEE_PRICE + tea * TEA_PRICE + sandwich * SANDWICH_PRICE
    RETURN total
END FUNCTION

FUNCTION print_receipt(name, coffee, tea, sandwich, total)
    OUTPUT "===== RECEIPT ====="
    OUTPUT "Customer : " + name
    OUTPUT "Coffee   : " + coffee
    OUTPUT "Tea      : " + tea
    OUTPUT "Sandwich : " + sandwich
    OUTPUT "-------------------"
    OUTPUT "Total = RM " + total (2 decimal places)
END FUNCTION

MAIN
    INPUT name
    INPUT coffee      // repeat until it is a whole number >= 0
    INPUT tea         // repeat until it is a whole number >= 0
    INPUT sandwich    // repeat until it is a whole number >= 0

    total = calculate_total(coffee, tea, sandwich)
    print_receipt(name, coffee, tea, sandwich, total)
END MAIN
```

---

## 4. The Code

### 4.1 `utils.py`: the logic functions

- `calculate_total(coffee, tea, sandwich)` multiplies each quantity by its price and returns the sum.
- `print_receipt(name, coffee, tea, sandwich, total)` prints the receipt. The five missing parameters in the template are the **name**, the **three quantities**, and the **total**.
- `get_quantity(prompt)` is an extra helper. It keeps asking until the user enters a valid whole number of 0 or more, which enforces the constraints in 1.5.

### 4.2 `main.py`: runs the program

`main.py` imports the functions from `utils.py` and runs them in order: input, then calculate, then print the receipt.

```python
from utils import get_quantity, calculate_total, print_receipt
```

Run it with:

```bash
python main.py
```

### Test Run (sample input from the tutorial)

```
Customer name: Bobby
Coffee quantity: 3
Tea quantity: 3
Sandwich quantity: 2

===== RECEIPT =====
Customer : Bobby
Coffee   : 3
Tea      : 3
Sandwich : 2
-------------------
Total = RM 67.50
```

**Checking the total by hand:**

| Item | Qty | Price | Subtotal |
|---|---:|---:|---:|
| Coffee | 3 | 8.50 | 25.50 |
| Tea | 3 | 6.00 | 18.00 |
| Sandwich | 2 | 12.00 | 24.00 |
| **Total** | | | **67.50** |

### Test Run (invalid input)

```
Coffee quantity: -1
Quantity cannot be negative. Try again.
Coffee quantity: abc
Please enter a whole number (e.g. 0, 1, 2).
Coffee quantity: 1
```

The program doesn't crash on bad input. It asks again until it gets a valid quantity.
