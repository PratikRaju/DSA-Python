arr=[[1,5,3],[4,0,2],[0,9,1]]
row=len(arr)
col=len(arr[0])
row_track=[0 for _ in range(row)]
col_track=[0 for _ in range(col)]
for i in range(0,row):
    for j in range(0,col):
        if arr[i][j]==0:
            row_track[i]=-1  
            col_track[j]=-1  
for i in range(0,row):
    for j in range(0,col):
        if row_track[i]==-1 or col_track[j]==-1:
            arr[i][j]=0
print(arr)