j=1
for i in range (1,5,1):
    p=i
    while(p<4):
        print(" ",end="")
        p+=1
    while(i!=0):
        print(j,end="")
        j+=1
        i-=1
    print()