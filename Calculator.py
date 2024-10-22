def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Not valid can't divided by 0"
    else:
        return x / y

def calculator():
    print("Perform  operations....:")
    print("1... Addition")
    print("2... Subtraction")
    print("3... Multiplication")
    print("4... Divide")

    select = input("Select the operation (1, 2, 3, 4): ")

    if select in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if select == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")

        elif select == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")

        elif select == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")

        elif select == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("ERROR!!!  INVAILED!!!")


calculator()
