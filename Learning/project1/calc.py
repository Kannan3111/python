def addition(num1, num2):
    return num1 + num2
def multiplication(num1, num2):
    return num1 * num2
def subtraction(num1, num2):
    return num1 - num2
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

print(addition(5, 3))