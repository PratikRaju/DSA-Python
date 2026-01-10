arr=[1,1,1,2,2,2,3,3,4,5,6,6,7]
n=len(arr)
i=0
j=i+1
if n==1:
    print("1")
while j<n:
    if arr[i]!=arr[j]:
        i+=1
        arr[i],arr[j]=arr[j],arr[i]
    j+=1
print(arr)