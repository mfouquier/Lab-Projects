def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2


def calculator():
    keep_calculating = True
    first_number = int(input("What's the first number? "))
    while keep_calculating:
        math_ops = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }
        
        for char in math_ops:
            print(char)
        operation = input("Pick an operation: ")
        second_number = int(input("What's the next number? "))

        if second_number == 0 and operation == '/':
            print("You can't divide by 0!!!")
        else:
            answer = math_ops[operation](first_number, second_number)
            print(f"{first_number} {operation} {second_number} = {answer}")
        

        another_calc = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()

        if another_calc == 'y':
            first_number = answer
        else: 
            keep_calculating = False
            print("\n" * 20)
            calculator()

calculator()