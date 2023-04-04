n=int(input("Enter the number:"))

# method 1
for i in range(n):#row
    for j in range(i+1):#coloumn
        print("*",end="")
    print(" ")


print("------------------------\n\n")
#method 2
for i in range(1,n+1):
    print("*"*i)

print("-------------------------------\n\n")
#method 1(inverse digonal)
for i in range(n,0,-1):#row
    for j in range(i):#coloumn
        print("*",end="")
    print(" ")


print("------------------------\n\n")
#method 2(inverse digonal)
for i in range(n,0,-1):
    print("*"*i)

