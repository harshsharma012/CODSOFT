def calculator():
    print("Welcome to calsi which perform a simple arithmetic operation")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return

    print("Choose  operation:")
    print("add. Addition (+)")
    print("sub. Subtraction (-)")
    print("mul. Multiplication (*)")
    print("div. Division (/)")
    
    operation = input("Enter the name of the operation (add/sub/mul/div): ")


    if operation == 'add':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == 'sub':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == 'mul':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error Division by zero is not allowed.")
    else:
        print("Invalid operation choice! Please choose a valid operation.")

calculator()
