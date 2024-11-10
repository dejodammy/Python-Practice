from hangmanart import *  

def addition(num1, num2):
    num3 = num1 + num2
    print(f"The answer is: {num3} ")
    return num3

def subtraction(num1, num2):
    num3 = num1 - num2
    print(f"The answer is: {num3} ")
    return num3

def multiplication(num1, num2):
    num3 = num1 * num2
    print(f"The answer is: {num3} ")
    return num3

def division(num1, num2):
    num3 = num1 / num2
    print(f"The answer is: {num3} ")
    return num3

def calculation(operation, num1, num2):
    if operation == "add":
        return addition(num1, num2)
    elif operation == "div":
        return division(num1, num2)
    elif operation == "mult":
        return multiplication(num1, num2)
    elif operation == "sub":
        return subtraction(num1, num2)
    else:
        print("Invalid operation")
        return None

def main():
    print(calculator)
    num1 = 0
    num2 = 0
    num3 = 0
    while True:
        operation = input("Input add, sub, mult, div for the operation: ").strip().lower()
        
        if operation in ["add", "sub", "mult", "div"]:
            if num1 == 0:
                num1 = int(input("Input first number: "))
            num2 = int(input("Input second number: "))
            
            num3 = calculation(operation, num1, num2)
                            
            continue_with_value = input("Do you want to continue with this value? Yes/No: ").strip().lower()
            if continue_with_value == "yes":
                num1 = num3
            else:
                num1 = 0
                num2 = 0
        else:
            print("Invalid operation. Please enter add, sub, mult, or div.")
        end_operatio = str(input("Do you want to continue or end caclulation Yes or No: ")).strip().lower()
        if end_operatio == "yes":
            print("Shutting down ... ")
            return

if __name__ == "__main__":
    main()

