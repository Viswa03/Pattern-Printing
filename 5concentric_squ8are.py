# concentric square
"""
if n=3 => 3*2-1= 5
 row=coloumn=5
 
if n=4 => 4*2-1= 7
 row=coloumn=7
 """
n=int(input("Enter no:"))
size=n*2-1
min=0
max=size-1
val=n #user given number
mat=[[0 for i in range(size)] for j in range(size)]

for i in range(n): #top
    for j in range(min,max+1):
        mat[i][j]=val
    for j in range(min+1,max+1): #left
        mat[j][i]=val
    for j in range(min+1,max+1): #bottom
        mat[max][j]=val
    for j in range(min+1,max): #right
        mat[j][max]=val
    min+=1
    max-=1
    val-=1
        

for i in range(size):
    for j in range(size):
        print(mat[i][j],end="")
    print()
