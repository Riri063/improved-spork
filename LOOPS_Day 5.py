numbers = [1, 2, 3, 4, 5] # list
for number in numbers: # number is a variable that stores the current value in the list
    print(number)
    for number in range(5):
         print(number)
print()
print()
print()
print()
for number in range(1,5):
      print (number)

      #ASSIGNMENT
      PWD = "BTS"
      failed_attempts = []
      for count in range (3):
            passwd = input("Enter password: ")
      if passwd == PWD:
            print("Access Granted")
            break
      else:
            failed_attempts.append("Failed Attempts")
print(failed_attempts)


PWD = "Tems"
failed_attempts = []
for count in range (3) :
      passwd = input("Enter password: ")
      if passwd == PWD:
            print("Acess Granted")
            break
      else:
            #append is used to add an item to the end of a list
            failed_attempts.append("Failed Attempt")
print(failed_attempts)