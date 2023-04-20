def binarySearch(arr,key):
    left=0
    right=len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=list(map(int,input("Enter values: ").split()))
arr.sort()
print (arr)
key=int(input("Enter key: "))
result=binarySearch(arr,key)

if result==-1:
    print("The number is not present")
else:
    print("the number is at: ",result)