n=int(input("enter your number"))
s=0
while n!=0:
    r=n%10
    s=r**2+s
    n=n//10
print(s)