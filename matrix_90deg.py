arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r=len(arr)
c=len(arr[0])
for i in range(0,r-1):
    for j in range(i+1,c):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
for i in range(0,r):
    arr[i].reverse()
print(arr)