import random;

random_number = random.randint(1,100)
print("I am thinking of a number between 1 and 100.")
user_Input=-1;
while user_Input != random_number:
    user_input = int(input("Enter a number between 1 and 100: "))
    if user_input > random_number:
        print("Your guess is too high. Try again.")
    elif user_input < random_number:
        print("Your guess is too low. Try again.")
    else:
        print("Congratulations! You guessed the number!")