    # MAKE SURE TO PUT A HINT OR SOME PART OF THE QUESTION  ON TOP OF THE ANSWER
    # 1. Determine Leap Year
    # Ask the user to enter a year and determine whether it is a leap year or not.
    # (A leap year is divisible by 4, but not by 100 unless also divisible by 400.)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
else:
        print(f"{year} is not a leap year")


    # 2. Grading System

    # Ask the user to enter their marks (0-100) and print the corresponding grade based on the following criteria:
    # 	•	Marks ≥ 90 → Grade A
    # 	•	Marks ≥ 80 → Grade B
    # 	•	Marks ≥ 70 → Grade C
    # 	•	Marks ≥ 60 → Grade D
    # 	•	Marks ≥ 50 → Grade E
    # 	•	Marks < 50 → Fail


grade = int(input("Enter your grade: "))
if grade >= 90:
        print("Congrats, Grade A")
elif grade >= 80:
        print("Congrats, Grade B")
elif grade >= 70:
        print("Congrats, Grade C")
elif grade >= 60:
        print("Congrats, Grade D")
elif grade >= 50:
        print("Congrats, Grade E")
else:
        print("Fail, try again!")


    # 3. Odd or Even

    # Ask the user to enter an integer and check whether it is odd or even.

num = int(input("Enter an integer: "))
if num % 2 == 0:
        print(f"{num} is even.")
else:
        print(f"{num} is odd.")

num = int(input("Enter an integer: "))
if num % 2 != 0:
        print(f"{num} is odd.")
else:
        print(f"{num} is even.")

        
# 4. Find the Greatest Number

# Ask the user to enter three numbers and determine which one is the greatest.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the greatest.")
elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the greatest.")
else:
        print(f"{num3} is the greatest.")

    # 5. Check Divisibility

    # Ask the user to enter a number and check whether it is divisible by both 5 and 11.

divisibility = int(input("Enter a number: "))
if divisibility % 5 == 0 and divisibility % 11 == 0:
        print(f"{divisibility} is divisible by both 5 and 11.")
else:
        print(f"{divisibility} is not divisible by both 5 and 11.")


    # 6. Voting Eligibility

    # Ask the user to enter their age. If the age is 18 or above, print “Eligible to vote”, otherwise print “Not eligible to vote”.

age = int(input("Enter your age: "))
if age >= 18:
        print("Eligible to vote")
else:
        print("Not eligible to vote")


    # 7. Electricity Bill Calculation

    # Ask the user to enter the number of units consumed and calculate the total bill using the following rate chart:
    # 	•	Up to 100 units: ₹5 per unit
    # 	•	101-300 units: ₹7 per unit
    # 	•	Above 300 units: ₹10 per unit
    # If the total bill exceeds ₹2000, apply a 5% surcharge.

units = int(input("Enter the number of units you used: "))
if units <= 100:
        bill = units * 5
elif units <= 300:
        bill = (100 * 5) + ((units - 100) * 7)
else:
        bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
if bill > 2000:
        surcharge = bill * 0.05
        bill += surcharge
        \

    # Print the final bill with 2 decimal places
print(f"Total bill amount: ₹{bill:.2f}")

    # 8. BMI Calculator

    # Ask the user to enter their weight (kg) and height (m). Calculate their Body Mass Index (BMI) using the formula:
    # BMI = \frac{\text{weight}}{\text{height}^2}
    # Print the BMI category based on the value:
    # 	•	BMI < 18.5 → Underweight
    # 	•	BMI 18.5 - 24.9 → Normal weight
    # 	•	BMI 25 - 29.9 → Overweight
    # 	•	BMI 30 and above → Obese



    # Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

    # Calculate BMI
bmi = weight / (height ** 2)

    # Print the BMI value
print(f"Your BMI is: {bmi:.2f}")

    # Determine the BMI category
if bmi < 18.5:
        print("Category: Underweight")
elif bmi < 25:
        print("Category: Normal weight")
elif bmi < 30:
        print("Category: Overweight")
else:
        print("Category: Obese")

    # 9. ATM Withdrawal

    # Ask the user to enter an amount to withdraw. Check if the amount is a multiple of 100. If it is, print “Transaction Successful”, otherwise print “Invalid amount. Please enter a multiple of 100.”

    # Ask the user for an amount to withdraw
amount = int(input("Enter the amount to withdraw: "))

    # Check if it's a multiple of 100
if amount % 100 == 0:
        print("Transaction Successful")
else:
        print("Invalid amount.")


    # 10. Triangle Type Checker

    # Ask the user to enter the three sides of a triangle. Determine and print whether the triangle is:
    # 	•	Equilateral (all sides equal)
    # 	•	Isosceles (two sides equal)
    # 	•	Scalene (all sides different)
    # Get sides of the triangle
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = float(input("Enter side C: "))

    # Determine the type of triangle
if a == b == c:
        print("This is an Equilateral triangle.")
elif a == b or a == c or b == c:
        print("This is an Isosceles triangle.")
else:
        print("This is a Scalene triangle.")
