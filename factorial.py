def factorial(n):
    if(n<=0):
        return 1
    else:
        multiply=n*factorial(n-1)
        return multiply

    

n=int(input("Enter number: "))
print(factorial(n))




    