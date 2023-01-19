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
-------------------------------------------------------------------------------------------------------------------

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
"""

money = int(input("enter how much money do you have :"))

if  money>=200 :
    print("you can buy chicken rice")
elif money<200 and money>=100 :
    print("you can buy rice and egg")
elif money<100 and money>=50 :
    print("CURD RICE")
else:
    print("LOW MONEY SO YOU CAN BUY ONLY BISCUTES")



