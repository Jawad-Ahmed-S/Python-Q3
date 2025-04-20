man = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
word = input("Enter a word")

guess = "";
alreadyFound = "";
i=0;
j=0;
while True:
    if len(guess) == len(alreadyFound):
      character = input("Guess a character : ")
      if character in word and character not in alreadyFound and len(man) > 0:
          guess += character
          print("Correct!")
          alreadyFound += character
          j+=1

      else:
          print("Incorrect!")
          man.pop();
          print("You have " + str(len(man)) + " tries left")
          print(man);
          i+=1
