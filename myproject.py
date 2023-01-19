import math

"""
n=int(input("enter number"))
c=(math.log2(n))
print(c)

num = int(input("enter the number :"))

if num%10==0:
    print("number "+str(num)+"is a multiple of 10 ")
else:
    print("number is not multiple of 10")

print("hi "*10)
"""

print("-" * 50)
year = int(input("enter the year :"))

if year != 0:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")
else:
    print("...please Enter valid year!.. ")
