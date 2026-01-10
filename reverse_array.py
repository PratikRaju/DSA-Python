arr=[3,25,24,5,89]
def rev(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
rev(arr)
print(arr)