
def safe_calc(num1, num2, opr):
    if opr == "+":
        return num1 + num2
    elif opr == "-":
        return num1 - num2
    elif opr == "*":
        return num1 * num2
    elif opr == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Division by zero is not allowed"
    else:
         return "Invalid operation"

while True:
    try:
        a = input("Enter a number (or 'quit' to exit): ') ")
        if a == "quit":
            print("Goodbye")
            break
        a = float(a)
        calc = input("Enter operation: ")
        b = input("Enter another number: ")
        b = float(b)
    except ValueError:
        print("Invalid input")
    else:
        print(f"Result = {safe_calc(a, b, calc)}")
    finally:
        print("Thank you for using the calculator!")

