num = int(input("Enter a number: "))

# Check if the number is prime
if num > 1:
    for i in range(2, int(num/2)+1):
        
        print("i:",i)
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
