import random

computer = random.choice(['rock', 'paper', 'scissors'])
user = input("Enter your choice (lowercase): ")
computerScore=0;
userScore=0;
if computer == user:
    print("It's a tie!")
else:
    
    if user == "rock":
        if computer == "scissors":
            print("You win! Rock smashes scissors.")
            userScore += 1
        else:  
            print("You lose! Paper covers rock.")
            computerScore += 1
    elif user == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
            userScore += 1
        else:  
            print("You lose! Scissors cut paper.")
            computerScore += 1
    elif user == "scissors":
        if computer == "paper":
            print("You win! Scissors cut paper.")
            userScore += 1
        else:  
            print("You lose! Rock smashes scissors.")
            computerScore += 1
    else:
        print("Invalid input! Please enter rock, paper, or scissors.")

print(f"Computer chose: {computer}")
print(f"Final score - You: {userScore}, Computer: {computerScore}")
