num = int(input("Enter the desired number to check: "))

# Check even or odd
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Check prime
if num < 2:
    print("not prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("prime")
    else:
        print("not prime")