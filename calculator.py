def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Example usage
num1 = 10
num2 = 2
result = divide(num1, num2)
print(f"{num1} divided by {num2} is: {result}")