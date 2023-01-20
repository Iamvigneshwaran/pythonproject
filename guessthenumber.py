import random

num = random.randint(1, 20)

guess = int(input("guess the number the number range 1 to 20 "))

attempt = 1
while True :
    if num != guess:
        if attempt != 4:
            if guess > num:
                print("your guess is grater..")
            else:
                print("your guess is lower...")
            attempt = attempt + 1
            guess = int(input("try again..."))
        else:
            print("maximam attempt reached... you lost")
            break
    else:
        print("you won")
        break


