import time;
import os;

minutes = int(input("Enter number of minutes for the countdown Timer: "))
seconds = int(input("Enter number of seconds for the countdown Timer: "))
if seconds<0 or minutes<0:
    print("Invalid Input!");
    exit();
elif seconds==0 and minutes==0:
    print("Time's up!");
    exit();
elif minutes>59:
    print("Invalid Input!");
    exit();
elif seconds >60:
    minutes += timerFor//60;
    seconds = timerFor%60;


def clrScreen():
    os.system('cls');

while seconds>0 or minutes>0:
    num=0;
    clrScreen();
    print(f"\n\n\t\tTime Remaining : ",str(minutes).zfill(2) ,": ", str(seconds).zfill(2));
    time.sleep(1);
    if(seconds==0):
        if minutes>0:
            minutes-=1;
            seconds=59;
    else:
        seconds-=1;
    
    
clrScreen();
print("Time's up!");


