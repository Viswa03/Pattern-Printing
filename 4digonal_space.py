n=int(input("ENTER THE NUMBER:"))
for i in range(n):
    for j in range(i+1):
        if j==0 or i==j or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")

print("______________________________\n\n\n")

for i in range(n,0,-1):
    for j in range(i-1):
        if j==0 or i==0 or i!=j:
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
