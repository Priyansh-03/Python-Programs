num=int(input("Enter number of terms: "))
a,b=0,1
if(num<=0):
    print("invalid input")
elif(num==1):
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        print(c)
        a,b=b,c
    