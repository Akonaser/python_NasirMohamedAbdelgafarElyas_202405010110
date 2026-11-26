# Student_Ave_Calc.py
# Tutorial 2 (Week 3) - Student Average Calculator
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110


# Input validation helper: keeps asking until the mark is a number from 0 to 100.
# Without it, typing "abc" or pressing Enter crashes the program with a ValueError,
# and impossible marks like 150 or -20 would be used in the average.
def get_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if 0 <= mark <= 100:   # also rejects "nan", because nan fails every comparison
            return mark
        print("Mark must be between 0 and 100.")


choice = "y"

# Iteration: keep repeating the whole process for each student
# as long as the user's choice is "y"
while choice == "y":

    # Sequence (input): ask the user for the three quiz marks.
    # get_mark() converts each one to a number with float() and checks it is 0-100
    quiz_1 = get_mark("Enter Quiz 1 mark: ")
    quiz_2 = get_mark("Enter Quiz 2 mark: ")
    quiz_3 = get_mark("Enter Quiz 3 mark: ")

    # Sequence (process + output): add the three marks, divide by 3
    # to get the average, then display it to 2 decimal places
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    print(f"Average mark: {average:.2f}")

    # Selection: an average of 50 or more is a pass, anything below 50 is a fail
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Ask whether to enter another student's marks.
    # .strip().lower()[:1] keeps only the first letter, so "Y", "y", "yes" and "Yes"
    # all become "y" and the loop continues
    choice = input("Continue? Select Y/N: ").strip().lower()[:1]

print("Program Ended")
