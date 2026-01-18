arr=[1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1]
count=0
max_count=0
for i in range(0,len(arr)):
    if arr[i]==1:
        count+=1
    if arr[i]==0:
        count=0
    if max_count<count:
        max_count=count
print(max_count)