# Made by: GabDaBegginer
# 10/22/2024

# Updated calculator program - Gab

import time

print("OPERATORS")
print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
""")

operator = input("Enter Operator (1/2/3/4/5): ")
print()

while True:
    if operator == "1":
        num1 = input("First number: ")
        num2 = input("Second number: ")
        
        while num1 == "" or num2 == "":
            print("Please enter a number for both inputs.")
            num1 = input("First number: ")
            num2 = input("Second number: ")

        sum = float(num1) + float(num2)
        print()
        print("Calculating...")
        time.sleep(2)
        print()
        print(f"{num1} + {num2} = {sum}")
        break
        
    elif operator == "2":
        num1 = input("First number: ")
        num2 = input("Second number: ")

        while num1 == "" or num2 == "":
            print("Please enter a number for both inputs.")
            num1 = input("First number: ")
            num2 = input("Second number: ")

        sum = float(num1) - float(num2)
        print()
        print("Calculating...")
        time.sleep(2)
        print()
        print(f"{num1} - {num2} = {sum}")
        break
        
    elif operator == "3":
        num1 = input("First number: ")
        num2 = input("Second number: ")

        while num1 == "" or num2 == "":
            print("Please enter a number for both inputs.")
            num1 = input("First number: ")
            num2 = input("Second number: ")

        sum = float(num1) * float(num2)
        print()
        print("Calculating...")
        time.sleep(2)
        print()
        print(f"{num1} × {num2} = {sum}")
        break
        
    elif operator == "4":
        num1 = input("First number: ")
        num2 = input("Second number: ")

        while num1 == "" or num2 == "":
            print("Please enter a number for both inputs.")
            num1 = input("First number: ")
            num2 = input("Second number: ")

        sum = float(num1) / float(num2)
        print()
        print("Calculating...")
        time.sleep(2)
        print()
        print(f"{num1} ÷ {num2} = {sum}")
        break
    
    elif operator == "5":
        print()
        print("Quitting program...")
        time.sleep(1)
        break
        
    elif operator == "":
        print("Please enter something numeric.")
        operator = input("Enter Operator (1/2/3/4/5): ")
        
    else:
        print(f"{operator}, is not an operator")
        print()
        print("Please enter only the operators available.")
        operator = input("Enter Operator (1/2/3/4/5): ")
