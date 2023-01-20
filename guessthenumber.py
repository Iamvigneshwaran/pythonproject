import random

num = random.randint(1, 20)

guess = int(input("guess the number the number range 1 to 20 "))

while num != guess:
    if guess > num:
        print("your guess is grater..")
    else:
        print("your guess is lower...")
    guess = int(input("try again..."))
print("you won")
