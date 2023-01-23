
# n=int(input("enter the number :"))
# i=2
# while i<=n:
#     if n%i == 0:
#         print(i)
#     i=i+1

# name = "vignesh"
# cricketers_list = ["virat","dhoni",]
# for i in name :
#     print(i)
#
# print("loop is completed...")

rowend = int(input("how many rows you want:"))
colend = int(input("how many columns you want:"))
char = input("enter character :")

for row in range(1, rowend+1):
    for col in range(1, colend+1):
        print(char, end=' ')
    print('')
