#grettest common divisor
def gdcfunction(num1, num2,num3):
    if num1 >num2:
        small = num2
    elif num1>num3:
        small=num3
    else:
        small= num1
    for i in range (1,small+1):
        if((num1%i==0) and (num2%i==0) and (num3%i==0)):
            gdc=i
    print(gdc)


gdcfunction(5,6,9)
