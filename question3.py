a =  int(input("enter the first value: "))
b = int(input("enter the second value: "))
operation = input("enter operation (+,-,*,/)")
# print(operation)
if operation == "+" :
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*" :
    print(a*b)
elif operation == "/" :
    print(a/b)
else: 
    print("enter valid operator")
    
 