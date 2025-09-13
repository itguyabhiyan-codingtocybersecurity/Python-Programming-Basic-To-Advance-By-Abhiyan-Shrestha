#Task 3
# Ask User for the number
# ask for another number
# ask user for the operation between those users (+,-,*,/)
# Product output as asked in task
# Done By Abhiyan Shrestha

def Calculator():
    Num1 = float (input("Enter First Number: "))
    Num2 = float (input("Enter Second Number: "))
    operator = input ("Enter Operator (+,-,*,/): ")

    if operator == "+":
        Result = Num1 + Num2
    
    elif operator == "-":
        Result = Num1 - Num2
    
    elif operator == "*":
        Result = Num1 * Num2
    
    elif operator == "/":
        Result = Num1 / Num2
    
    print ("Results:",Result)

Calculator ()