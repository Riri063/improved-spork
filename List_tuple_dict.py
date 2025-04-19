#List:
#What is a list?
#A list is a collection type that's used to store multiple values/data to a singke variable
#It is oreders, mutable and index(each element is given an index position that is used to uniquely identify that element)
#We can tell something is a list when we see '[]' with comma seperated values
#'[A, B, C, D]'

#            0        1         2
#fruits = ["Apple", "Banana", "Cherry"]
#numbers = [1,2,3,4,5,6,7]
#multi_list = [
    #["X", "O", "X"]
    #["X", "O", ""]


     
    

#List of names
names = ["Ade" , "Riyah" , "Rae"]

#Get user input
search_names = input("Enter a name: ")

#Check if the name is in the list
if search_names in names:
    print(f"{search_names} is in the list")
else:
    print(f"{search_names} is not in the list")




    
#List of passwords
passwords = ["A123" , "B456" , "C789"]

#Get user input
search_passwords = input("Enter a password: ")

#Check if the password is in the list
if search_passwords in passwords:
    print(f"{search_passwords} is in the list")
else:
    print(f"{search_passwords} is not in the list")

    

    response = input("Do you want to login?: ")
    if response == "yes" :
        print("Successful!""gig")

    else:
        print("Goodbye!")


utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")

#utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)
