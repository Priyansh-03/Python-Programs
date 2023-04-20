def selectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index]=arr[min_index],arr[i]



arr=list(map(int,input("Enter values: ").split()))
print (arr)
key=int(input("Enter key: "))
result=selectionSort(arr)
print("Sorted array: ", arr)