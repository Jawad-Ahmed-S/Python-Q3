year = int(input("Enter a year to check if it is a leap year : "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("It is a Leap Year")
        else:
            print("It is not a Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("It is not a Leap Year")