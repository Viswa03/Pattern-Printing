num=int(input("Enter no:"))
n_list=[[0 for i in range(num)] for j in range(num)]
n=1
min=0
max=num-1
val=int((num+1)/2) #itratition puropse if num=5 -> 3itration
for i in range(val):
    for j in range(min,max+1): #top
        n_list[i][j]=n
        n+=1
    for j in range(min+1,max+1): #right
        n_list[j][max]=n
        n+=1
    for j in range(max-1,min-1,-1): #bottom
        n_list[max][j]=n
        n+=1
    for j in range(max-1,min,-1): #left
        n_list[j][i]=n
        n+=1

    min+=1
    max-=1

for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print("\n")
