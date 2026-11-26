"""
Tutorial 1 - Movie Theater Admission
Name: Nasir Mohamed Abdelgafar Elyas
Student ID: 202405010110

Policy: a person may enter if
    (they are 13 or older OR accompanied by an adult) AND they have a valid ticket
"""

from itertools import product

MIN_AGE = 13


# ---------------------------------------------------------------
# 1. Identify the components
# ---------------------------------------------------------------
#   Inputs : age (int), accompanied (bool), has_ticket (bool)
#   Process: (age >= 13 OR accompanied) AND has_ticket
#   Output : "Entry Allowed" or "Entry Denied"

def show_components():
    print("=" * 50)
    print("1. COMPONENTS")
    print("=" * 50)
    print("Inputs : age (int), accompanied (bool), has_ticket (bool)")
    print(f"Process: (age >= {MIN_AGE} OR accompanied) AND has_ticket")
    print('Output : "Entry Allowed" or "Entry Denied"')
    print()


# ---------------------------------------------------------------
# 2. The algorithm
# ---------------------------------------------------------------

def can_enter(age, accompanied, has_ticket):
    """Return True if the person is allowed into the theater."""
    old_enough = age >= MIN_AGE
    return (old_enough or accompanied) and has_ticket


def decision(allowed):
    return "Entry Allowed" if allowed else "Entry Denied"


# ---------------------------------------------------------------
# 2.2 Truth table (generated, not typed by hand)
#     A = age >= 13, B = accompanied, C = has_ticket
# ---------------------------------------------------------------

def show_truth_table():
    print("=" * 50)
    print("2.2 TRUTH TABLE")
    print("=" * 50)
    print(" A  B  C | A OR B | (A OR B) AND C | Result")
    print("-" * 50)
    for a, b, c in product([True, False], repeat=3):
        a_or_b = a or b
        result = a_or_b and c
        t = lambda x: "T" if x else "F"
        print(f" {t(a)}  {t(b)}  {t(c)} |   {t(a_or_b)}    |       {t(result)}        | {decision(result)}")
    print()


# ---------------------------------------------------------------
# 3. Evaluate expression - test with input samples
# ---------------------------------------------------------------

TEST_SAMPLES = [
    # (age, accompanied, has_ticket, expected)
    (15, False, True, True),    # teen alone with ticket
    (10, True, True, True),     # child with adult and ticket
    (10, False, True, False),   # child alone
    (20, True, False, False),   # adult without ticket
    (13, False, True, True),    # boundary: exactly 13
    (12, False, True, False),   # boundary: just under 13
]


def run_tests():
    print("=" * 50)
    print("3. TEST SAMPLES")
    print("=" * 50)
    print(f"{'Age':>4} | {'Adult':<5} | {'Ticket':<6} | {'Result':<13} | Check")
    print("-" * 50)
    passed = 0
    for age, accompanied, has_ticket, expected in TEST_SAMPLES:
        result = can_enter(age, accompanied, has_ticket)
        ok = result == expected
        passed += ok
        print(f"{age:>4} | {str(accompanied):<5} | {str(has_ticket):<6} | "
              f"{decision(result):<13} | {'PASS' if ok else 'FAIL'}")
    print(f"\n{passed}/{len(TEST_SAMPLES)} tests passed\n")


# ---------------------------------------------------------------
# Interactive version (the pseudocode, in Python)
# ---------------------------------------------------------------

def read_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 120:
                return age
        except ValueError:
            pass
        print("Please enter a whole number from 0 to 120.")


def read_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    show_components()
    show_truth_table()
    run_tests()

    print("=" * 50)
    print("TRY IT YOURSELF")
    print("=" * 50)
    age = read_age()
    accompanied = read_yes_no("Accompanied by an adult? (y/n): ")
    has_ticket = read_yes_no("Has a valid ticket? (y/n): ")
    print(decision(can_enter(age, accompanied, has_ticket)))


if __name__ == "__main__":
    main()
