def table(num,i,Range):
     
     if (i > Range):
       return
   
     print(f"{num} x {i} = {num*i}")
     table(num,i+1,Range)

num=int(input("Enter your number : "))
Range=int(input("Enter the range : "))
print(f"Table of {num}")
table(num,1,Range)   
    
    