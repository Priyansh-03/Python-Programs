def linearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1


arr=list(map(int,input("Enter values: ").split()))
print (arr)
key=int(input("Enter key: "))
result=linearSearch(arr,key)

if result==-1:
    print("The number is not present")
else:
    print("the number is at: ",result)