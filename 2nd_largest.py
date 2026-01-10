arr=[50,-9,33,99,100,4]
large=float("-inf")
second_large=float("-inf")
n=len(arr)
for i in range(0,n):
    if large<arr[i]:
        second_large=large
        large=arr[i]
    elif arr[i]!=large and second_large<arr[i]:
        second_large=arr[i]
print(second_large)
        