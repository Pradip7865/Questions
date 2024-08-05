string1=str(input("Enter Any string "))
count=0
for i in string1:
    for j in string1:
        if(i==j):
            count+=1
        if count>1:
            break
    if count==1:
        print(i,end=" ")