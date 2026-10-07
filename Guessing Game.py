import random

def game(max):
    num = random.randint(1,100)
    guess = int(input("Guess the number: "))
    while guess != num: 
        if guess > num: 
            print("Too high. Try again")
        if guess < num: 
            print("Too low. Try again")
        guess = int(input("Guess the number: "))
        tries += 1
        if tries >= max:
            print("You're out of lives!")
            break
    else:
        print(f"That's correct! You got it in {tries} tries")
        break


guess = 0
tries = 0
while True:
    print("-Guessing Game-")
    choice = int(input("""
        1. Play new game
        2. Exit
    """))
    if choice == 1:
        diff = int(input("""
        Choose difficulty:
        1. Easy
        2. Medium
        3. Hard
        """))
        if diff == 1:
            game(9)
        elif diff == 2:
            game(8)
        elif diff == 3:
            game(7)
        
        # num = random.randint(1,100)
        # guess = int(input("Guess the number: "))
        # while guess != num: 
        #     if guess > num: 
        #         print("Too high. Try again")
        #     if guess < num: 
        #         print("Too low. Try again")
        #     guess = int(input("Guess the number: "))
        #     tries += 1
        #     if tries >= 7:
        #         print("You're out of lives!")
        #         break
        # else:
        #     print(f"That's correct! You got it in {tries} tries")
        #     break
    elif choice == 2:
        break
