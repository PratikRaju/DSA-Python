arr=[2,3,4,5,1,6]
n=len(arr)
target=9
dic={}
for i in range(0,n-1):
    diff=target-arr[i]
    if diff in dic:
        print([dic[diff],i])
    else:
        dic[arr[i]]=i