a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c= int(input("enter the value of c: "))
if(a > b and b > c):
    print("a is greatest among three")
elif(b > c and b > a):
    print("b is the greates among three")
elif(c > b and c > a):
    print("c is the greatest among three ")