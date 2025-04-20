user_input = int(input("Enter a number: (less than 100) "))

while user_input > 100:
    print("Invalid number. Please enter a number less than 100.")
    user_input = int(input("Enter a number: (less than 100) "))

current_number = user_input;

while current_number<100:
    print(current_number)
    current_number = current_number*2;

    print(current_number);