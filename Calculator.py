def nextOperation():
    print("Type your next operation: 1) Equal 2) Addition 3) Subtraction 4) Multiplication 5) Division 6) Modulus 7) Exponent 8) Root")

num1 = int(input("Enter your first number:"))

nextOperation()
oper = int(input())

while oper != 1:
    num2 = int(input("Enter your next number "))

    if oper == 2: # Addition
        num1 += num2
    elif oper == 3: # Subtraction
        num1 -= num2
    elif oper == 4: # Multiplication
        num1 *= num2
    elif oper == 5: # Division
        num1 /= num2
    elif oper == 6: # Modulus
        num1 %= num2
    elif oper == 7: # Exponent
        num1 = pow(num1, num2)
    elif oper == 8: # Root
        num1 = pow(num1, 1/num2)
    else:
        print("Please type a provided number")
   
    nextOperation()
    oper = int(input())

print("Your answer is: " + str(num1))
