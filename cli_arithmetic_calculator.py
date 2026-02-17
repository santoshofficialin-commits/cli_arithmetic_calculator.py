# mini calculater for daily use with using arithmetic operators and conditional keywords
num1 = float(input("Enter Your First Number : "))
num2 = float(input("Enter Your Second number : "))
OP = input("Enter Your Operator( +, -, *, /, %, //) : ")
if OP ==  "+"  :
    print("Result : ", num1 + num2)
elif OP == "-" :
    print("Result : ", num1 - num2)
elif OP == "*" : 
    print("Result : ", num1 * num2)
elif OP == "/" :
    print("Result : ", num1 / num2)
elif OP == "%" :
    print("Result : ", num1 % num2)
elif OP == "//" :
    print("Result : ", num1 // num2)
else :
    print("Invalid Operator")