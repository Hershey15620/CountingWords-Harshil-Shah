letterlist= input("enter string-")
Ccount=0
Wcount=1
for i in letterlist: 
    Ccount= Ccount + 1
    if (i==" "):
        Wcount=Wcount + 1
print("number of words in the string", Wcount)
print ("number of characters in the string", Ccount)
