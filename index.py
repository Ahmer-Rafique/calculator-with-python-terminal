print("Welcome to our Calculator")
while True:
    first_number = int(input("Please enter your first number: "))
    second_number = int(input("Please enter your second number: "))

    operations = int(input("Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division, 5 for Modulus: "))

    if operations == 1:
        print(f"Your Addition result is: {first_number + second_number}")
    elif operations == 2:
        print(f"Your Subtraction result is: {first_number - second_number}")
    elif operations == 3:
        print(f"Your Multiplication result is: {first_number * second_number}")
    elif operations == 4:
        if second_number != 0:
            print(f"Your Division result is: {first_number / second_number}")
        else:
            print("Division by zero is not allowed!")
    elif operations == 5:
        print(f"Your Modulus result is: {first_number % second_number}")
    else:
        print("Invalid operation selected! Please choose a valid option.")

    continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice == "no":
        print("Thank you for using the calculator. Goodbye!")
        break
    elif continue_choice != "yes":
        print("Invalid input. Assuming you want to exit. Goodbye!")
        break
