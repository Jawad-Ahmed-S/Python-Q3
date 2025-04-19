import random
num = input("Enter a number for the computer to guess: ")
iteration=0;
while(int(num) != random.randint(1, 100)):
    print("The computer guessing!")
    iteration+=1

print("The computer guessed the number correctly in " + str(iteration) + " iterations!");