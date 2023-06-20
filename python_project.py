# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def main():
    print("Welcome to the calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        result = add(num1, num2)
        operation = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "/"
    else:
        print("Invalid choice!")
        return

    print(f"{num1} {operation} {num2} = {result}")

if __name__ == '__main__':
    main()
