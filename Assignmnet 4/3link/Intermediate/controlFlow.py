import random 
score=0;
YourNum=-1;
CompNum=-1;
UserChoice = "";
for i in range(10):
    print("Round ",i+1)
    YourNum = random.randint(1,100)
    print("Your number is ",YourNum)
    CompNum = random.randint(1,100)
    UserChoice = input("What do you think is your number higher or lower than computr's?")
    if UserChoice.lower() == "higher":
        if YourNum > CompNum:
            score = score + 1
            print("You are right")
            print("Computer's number is ",CompNum)
            print("Your score is ",score)
    else:
        print("You are wrong")
        print("Computer's number is ",CompNum)
        print("Your score is ",score)

