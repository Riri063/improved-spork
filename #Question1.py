# year= int(input("Enter a year:"))
# if (year % 4 == 0 and year % 100 !=0 ) or (year % 400 == 0):
#  print(f"{year} is a leap year")
# else:
#  print(f"{year} is not a leap year")

# grade= int(input("Enter your grade:"))
# if grade >= 90:
#  print("Congrats, Grade A")
# if grade >= 80:
#  print("Congrats, Grade B")
# if grade >= 70:
#  print("Congrats, Grade C")
# if grade >= 60:
#  print("Congrats, Grade D")
# if grade >= 50:
#  print("Congrats, Grade E")
# else:
#  print("Fail, try again!")

# num = int(input("Enter an integer: "))

# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")

# num = int(input("Enter an integer:"))
# if num % 2 != 0:
#     print(f"{num} is odd.")
# else:
#     print(f"{num} is even.")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the greatest.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the greatest.")
# else:
#     print(f"{num3} is the greatest.")

# divisibility= int(input("Enter a number"))

# if divisibility % 5 == 0 and divisibility % 11 == 0:
#     print(f"{divisibility} is divisible by both 5 and 11.")
# else:
#     print(f"{divisibility} is not divisible by both 5 and 11.")

# age= int(input("Enter your age"))
# if age >= 18:
#  print("Eligible to vote")
# else:
#  print("Not eligible to vote")

# units= int(input("Enter the number of units you used"))
# if units <= 100:
#     bill = units * 5
# elif units <= 300:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
# if bill > 2000:
#     surcharge = bill * 0.05
#     bill += surcharge

# # Print the final bill with 2 decimal places
# print(f"Total bill amount: ₹{bill:.2f}")

# Get user input
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))

# # Calculate BMI
# bmi = weight / (height ** 2)

# # Print the BMI value
# print(f"Your BMI is: {bmi:.2f}")

# # Determine the BMI category
# if bmi < 18.5:
#     print("Category: Underweight")
# elif bmi < 25:
#     print("Category: Normal weight")
# elif bmi < 30:
#     print("Category: Overweight")
# else:
#     print("Category: Obese")

# # Ask the user for an amount to withdraw
# amount = int(input("Enter the amount to withdraw: "))

# # Check if it's a multiple of 100
# if amount % 100 == 0:
#     print("Transaction Successful")
# else:
#     print("Invalid amount.")

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

