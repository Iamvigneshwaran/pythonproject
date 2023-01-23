# num1 = input("enter the number")
# num2 = input("enter the number ")
# num3 = int(num1+num2)
# print(num3-int(num1))
# ---------------------------------

# Initialize a list with some elements
my_list = [1, 2, 3, 4, 5]

# Iterate over the list and print each element
for item in my_list:
    if item % 2 == 0:
        print(item, "is even.")
    else:
        print(item, "is odd.")

# Prompt the user for a number and check if it's in the list
user_input = int(input("Enter a number: "))
if user_input in my_list:
    print(user_input, "is in the list.")
else:
    print(user_input, "is not in the list.")
