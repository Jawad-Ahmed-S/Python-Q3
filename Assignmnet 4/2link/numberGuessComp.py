import random
guess = input("Guess the number between 1 - 100");

num = random.randint(1, 100);

if guess == num:
    print("You guessed the number correctly!")
else:
    print("You guessed the wrong number!")