'''name = "vignesh waran"
str = "Happy"

print(str[:-3:-1])
print(name[::-2])

number = 1

while number <= 20:
    if number % 2 == 0:
        print("number is", number)
    number = number + 1
'''




while True :
    number = input("enter the number between 1 to 10:")
    if number.isnumeric() and 1< int(number) <=10 :
        print ("you enter a valid number ",number)
        break
    else :
        print("!!!please enter a valid number")
print ("loop is completed")