arr=[3,4,4,4,8,9,9,10,12,12,14,15]
target=6
n=len(arr)
floor=-1
ceil=-1
l=0
h=n-1
while l<=h:
    mid=(l+h)//2
    if arr[mid]==target:
        floor=arr[mid]
        ceil=arr[mid]
        break
    elif arr[mid]>target:
        ceil=arr[mid]
        h=mid-1
    else:
        floor=arr[mid]
        l=mid+1
print([floor,ceil])
        