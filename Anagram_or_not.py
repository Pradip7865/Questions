string1="pradip"
string2="pradip"
if(len(string1)!=len(string2)):
    print("Not anagram")
else:
    string1=sorted(string1)
    string2=sorted(string2)
    if(string1==string2):
        print("is anagram")
    else:
        print("not anagram")