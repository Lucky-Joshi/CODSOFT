#Function for Addition.
def add(x, y):
    return x + y

#Function for Subtraction.
def subtract(x, y):
    return x - y

#Function for Multiplication.
def multiply(x, y):
    return x * y

#Function for Division.
def divide(x, y):
    if y == 0:
        return "Error! Division by zero." # Error handling in case divisor is 0
    else:
        return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thanks for using our Calculator")
            break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")