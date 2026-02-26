arr=[1,99,101,98,2,5,3,100,1,1]
arr.sort()
last_smaller=float("-inf")
count=0
large=0
n=len(arr)
for i in range(0,n):
    num=arr[i]
    if num-1==last_smaller:
        count+=1
        last_smaller=num
    elif num!=last_smaller:
        count=1
        last_smaller=num
    large=max(large,count)
print(large)
