# Student_Ave_Calc.py
# Tutorial 2 (Week 3) - Student Average Calculator
# Name: Nasir Mohamed Abdelgafar Elyas
# Student ID: 202405010110

choice = "y"

# Iteration: keep repeating the whole process for each student
# as long as the user's choice is "y"
while choice == "y":

    # Sequence (input): ask the user for the three quiz marks
    # and convert each one from text to a number with float()
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

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
    # .strip().lower() turns "Y", " y " etc. into "y" so the loop check still works
    choice = input("Continue? Select Y/N: ").strip().lower()

print("Program Ended")
