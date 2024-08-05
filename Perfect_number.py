n1=496 #6,8128 etc
temp=0
for i in range (1,n1):
    if(n1%i==0):
        temp=temp+i
if(temp==n1):
    print("perfect number")
else:
    print("Not perfect")