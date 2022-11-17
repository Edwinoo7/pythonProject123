n=int(input("Enter the limit"))
list=[]
print("Enter the digits")
for i in range(0,n):
    ele=int(input())
    if ele>100:
        list.append("Over")
    else:
        list.append(ele)
print(list)