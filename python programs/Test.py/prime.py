f=0
n=int(input("Enter your number"))
for i in range (2,n):
    if n%i==0:
        f=1
        break
if f==1:
    print("Number is not prime ")
else:
    print(n," is prime")
        
    