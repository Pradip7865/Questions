def replacearr(arr):
    newarry=arr.copy()
    newarry.sort()
    for i in range(len(arr)):
        for j in range(len(newarry)):
            if (arr[i]==newarry[j]):
                arr[i]=j+1
                break

arr1=[4,8,25,36,1,25]
print("original array ",arr1)
replacearr(arr1)
print("replaced array ",arr1)