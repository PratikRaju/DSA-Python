arr=[4,5,6,7,8,0,1]
n=len(arr)
l=0
h=n-1
while l<h:
    mid=(l+h)//2
    if arr[mid]>arr[h]:
        l=mid+1
    else:
        h=mid
print(arr[l])