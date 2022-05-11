import random

print("number guessing game")
number = random.randint(1,9)

chances = 0
while chances<5:
    guess = int(input("enter your guess"))

    if guess == number:
        print("Congratulations Your Won!")
        break
    elif guess < number:
        print("Your guess was too lows",guess)
    else:
        print("Your guess was too hight",guess)
    chances +=1    
if chances > 5:
    print("You Lose!!!the number is",number) 