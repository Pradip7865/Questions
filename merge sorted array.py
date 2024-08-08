def bubblesort(temp):
    total=len((temp))
    for i in range (total):
        for j in range (0,total-i-1):
            if(temp[j]>temp[j+1]):
                temp[j],temp[j+1]=temp[j+1],temp[j]
                
    return temp

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
temp=[]
for i in range(len(nums1)):
    if (nums1[i]!=0):
        temp.append(nums1[i])

for i in range(len(nums2)):
    if (nums2[i]!=0):
        temp.append(nums2[i])
print("Merge list ",temp)
print("Ascending Order list ",bubblesort(temp))