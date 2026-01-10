arr=[55,32,-97,99,3,670]
large=arr[0]
n=len(arr)
for i in range(0,n):
    if large<arr[i]:
        large=arr[i]
print(large)