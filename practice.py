#Criteria  = ("Admin" "User" "Guest" "Super_Admin"
#"Moderator")
#RANDO ="HACKER"
#try:
   # Criteria[0] = RANDO 
#except TypeError as e:
    #print("TypeError: ",e)
    #print ("Hey Someone is trying to hack into the system")





#Boolean results
# '==' is the equality operator that is used to check that 2 values are actuall equal


#Code from day 3
key = 5
data =10

value = (key == data)
print(value)

if key == data:
    print("Key and data are equal")
    print("Access granted")

logins = 10
attempts =3
value2 = (attempts < logins)
print(value2)

expected_key = "anything"
actual_key = "k"
value3 = (expected_key != actual_key)
name = input("Name?")
print("HI", name)
password = input("Enter password(>= 8 chars): ")
if len(password) >= 8:
    print("Password is valid")
else:
    print("Password is invalid")

    #You habe been given a evice, dial any of the code to accept your mission

phone = input("Enter 1) Blue Pill  2) Red Pill  3) Yellow Pill  4) Green Pill")
if phone == "1":
    print("You have chosen the Blue Pill")
elif phone == "2":
    print("You have chosen the Red Pill")
elif phone == "3":
    print("You have chosen the Yellow Pill")
elif phone == "4":
    print("You have chosen the Green Pill")
else:
    print("Invalid choice")   

































"""
Variables: Containers for storing data values.
 In other programming languages, you'd have to specify the data-type you want for a particular variable 
But in python, you don't have to specify the data-type you want for a aparticular `
Mneumonic Variale naming
you name a variable in such a a way that it gives you a hint of what the variable represents 



"""