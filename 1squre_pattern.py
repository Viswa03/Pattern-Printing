"""
#method1
n=int(input("Enter the number:"))
for i in range (n):
    for j in range (n):
        print("*",end="")
    print("")
"""
#method2
n=int(input("Enter the number:"))
for i in range (n):
    print("*"*n)
