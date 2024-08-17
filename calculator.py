def add(x, y):
    return x + y

def calculator():
    print("Select operation:")
    print("1. Add")

    choice = input("Enter choice (1): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"{num1} + {num2} = {add(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Example usage
num1 = 10
num2 = 2
result = divide(num1, num2)

print(f"{num1} divided by {num2} is: {result}")
print(f"{num1} divided by {num2} is: {result}")
