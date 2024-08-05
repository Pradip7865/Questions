def bubblesort(arr):
    total=len(arr)
    for i in range (total):
        for j in range (0,total-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return arr


arr=[25,36,25,56,89,14,21,12]
print("original array ",arr)
print("sorted array ",bubblesort(arr))
        