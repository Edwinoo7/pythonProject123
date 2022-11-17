
str=input("enter the data")
dict={}
for n in str:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
for m,n in dict.items():
    print(m,n)