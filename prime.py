
num = int(input("enter the value: "))
if num <= 1:
    print("neither prime nor composite ")
else:
    for i in range (2,num):
        if num % i == 0:
            print("number is composite")
            break
    else:
         print("number is prime")