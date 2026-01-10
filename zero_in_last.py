arr=[1,2,3,4,5,6,7]
i=0
n=len(arr)
while i<n:
    if arr[i]==0:
        break
    i+=1
if i==n:
    print("There is no zeros in array")
j=i+1
while j<n:
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    j+=1
print(arr)