import random

secret= random.randint(1,20)
tries=0
max_tries=4

while tries<max_tries:
    guess=int(input("guess a number(1-20):"))
    tries+=1

    if guess==secret:
        print("You got it in {tries} tries!")

    elif guess<secret:
        print("too low")

    else:
     print("too high")

else:
    print(f"out of tries, the number was {secret}")