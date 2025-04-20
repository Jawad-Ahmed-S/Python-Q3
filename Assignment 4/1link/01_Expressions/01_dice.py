import random as r
def roll_dice():
    dice1 = r.randint(1,6);
    dice2 = r.randint(1,6);
    total = dice1 + dice2;
    print("Total of dice : ",total);
def main():
    dice1 = 10;
    print("Dice 1 (in main): ",dice1);
    roll_dice();
    roll_dice();
    roll_dice();
    print("Dice 1 (in main): ",dice1);

    main();