a = int(input("Enter 1 Number:-\n"))
b = int(input("Enter 2 number:-\n"))
Choose_operator =input("choose operation:-\n")
if Choose_operator == '+':
    print(a+b)
elif Choose_operator == '-':
    print(a - b)
elif Choose_operator == '*':
    print(a*b)
elif Choose_operator == '/':
    print(round(a/b, 2))
elif Choose_operator == '%':
    print(a%b)
else:
    print("Please Enter Invalid Choice")
