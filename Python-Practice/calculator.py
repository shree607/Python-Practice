a = float(input(print("Enter the first number: ")))
operator = input("Enter the operator (+, -, *, /)")
b = float(input(print("Enter the second number: ")))
if operator == "+":
    print ("Result: ", a+b)
elif operator == "-":
    print ("Result: ", a-b)
elif operator == "*":
    print ("Result: ", a*b)
elif operator == "/":
    if b != 0:
        print ("Result: ", a/b)
    else:
        print("Number cannot be divided by zero")
else:
    print("Invalid input!!")

