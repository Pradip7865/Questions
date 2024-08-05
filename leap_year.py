def leapyaer(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year=2020
if leapyaer(year):
    print(year,"is leap yaer")
else:
    print(year,"not leap yaer")