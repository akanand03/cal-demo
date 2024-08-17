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
