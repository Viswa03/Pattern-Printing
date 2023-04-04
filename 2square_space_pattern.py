n=int(input("Enter the number:"))
for i in range(n):#row
    for j in range(n):#coloumn
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
        
