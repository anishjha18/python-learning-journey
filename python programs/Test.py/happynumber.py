n=int(input("Enter any number"))#31
while n%10!=n: #1!=31
    s=0
    while n>0:#31>0
        r=n%10#1
        s=s+r**2#1
        n=n//10#3
    n=s
if n==1:
    print("happy no")
else:
    print("not happy no")