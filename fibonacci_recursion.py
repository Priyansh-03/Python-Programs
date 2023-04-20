def fibonacci(n):
    if(n<=0):
        return None
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n=int(input("Enter number of terms: "))
for i in range(1, n+1):
    print(fibonacci(i))




    