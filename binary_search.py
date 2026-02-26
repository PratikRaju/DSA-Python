#Iterative method
def b_search(arr,target):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[1,2,3,4,5,6,7,8]
t=6
ans=b_search(arr,t)
print(ans)
#Recursive method
def b_search(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return b_search(arr,target,mid+1,high)
    else:
       return b_search(arr,target,low,mid-1)
arr=[1,2,3,4,5,6,7,8]
t=60
l=0
h=len(arr)-1
ans=b_search(arr,t,l,h)
print(ans)        