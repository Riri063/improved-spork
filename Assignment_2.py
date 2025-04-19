# year= int(input("Enter a year:"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap yaer")

# grade= int(input("Enter your grade:"))

# if grade >= 80:
#     print("Grade A")
# elif grade >= 70:
#     print("Grade B")
# elif grade >= 60:
#     print("Grade C")
# elif grade >= 50:
#     print("Grade D")
# else:
#     print("Fail")

# number=int(input("Enter a number:"))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# number3 = int(input("Enter third number: "))

# greatest = max(number1, number2, number3)

# print(f"The greatest number is: {greatest}")                                                                            

# number= int(input("Enter a number"))
# if (number % 5 == 0 and number % 11 == 0):
#     print("The number is divisible")
# else:
#     print("The number is not divisible")

# def calculate_electricity_bill():
#     units = int(input("Enter the number of units consumed: "))
    
#     if units <= 100:
#         bill = units * 5
#     elif units <= 300:
#         bill = (100 * 5) + ((units - 100) * 7)
#     else:
#         bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

#     if bill > 2000:
#         bill += bill * 0.05  # 5% surcharge
    
#     print(f"Total Electricity Bill: ₹{bill:.2f}")
#     calculate_electricity_bill()


# 

        
# # Electricity Bill Calculation

# # Prompt the user to enter the number of units consumed
# units = int(input("Enter the number of units consumed: "))

# # Initialize the bill amount to 0
# bill = 0

# # Calculate the bill based on the number of units consumed
# if units <= 100:
#     bill = units * 5
# elif units <= 300:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# # Apply a 5% surcharge if the bill exceeds ₹2000
# if bill > 2000:
#     surcharge = bill * 0.05
#     bill += surcharge

# # Display the total bill amount
# print(f"Total Electricity Bill: ₹{bill:.2f}")

amount= int(input("Enter an amount to withdraw: "))
if amount % 100 == 0:
    
            print("Transaction Successful")
else:
            print("Invalid amount. Please enter a multiple of 100.")
