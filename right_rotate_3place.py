def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
arr=[1,2,3,4,5,6,7]
k=3
n=len(arr)
reverse(arr,n-k,n-1)
reverse(arr,0,n-k-1)
reverse(arr,0,n-1)
print(arr)