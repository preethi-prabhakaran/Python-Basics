# Implement Calculator (Basic Operations) with OOPS

import math


class MultipleOperatorOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1


class SingleOperatorsOperations:
    def __init__(self, num):
        self.num = num

    def square_root(self):
        if self.num >= 0:
            return self.num ** 0.5
        else:
            return "Error! You are trying square root of a negative number"

    def factorial(self):
        return math.factorial(self.num)


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Square Root")
    print("4. Factorial")

    choice = input("Enter choice from the menu above (1/2/3/4):")

    if choice in ['1', '2']:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
        mo = MultipleOperatorOperations(num1, num2)
        if choice == '1':
            print(f'{num1}+{num2} = {mo.add()}')
        elif choice == '2':
            print(f'{num2}-{num1} = {mo.subtract()}')
    elif choice in ['3', '4']:
        num1 = int(input("Enter the number: "))
        so = SingleOperatorsOperations(num1)
        if choice == '3':
            print(f"Square root of a number = {so.square_root()}")
        elif choice == '4':
            print(f"Factorial of {num1}= {so.factorial()}")

    else:
        print("Invalid input")


while True:
    calculator()
    user_choice = input("Do you want to perform another calculation(yes/no):")
    if user_choice != 'yes':
        break
