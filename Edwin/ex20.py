n=int(input())
a=0
b=1
if n<=0:
    print("not")
elif n==0:
    print("0")
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)