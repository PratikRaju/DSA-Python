arr=[1,3,4,5,6,7,8,9]
target=2
n=len(arr)
lb=0
ub=n
while lb<ub:
    mid=(lb+ub)//2
    if arr[mid]==target:
        print(mid)
    elif arr[mid]<=target:
        lb=mid+1
    else:
        ub=mid
print(lb)
