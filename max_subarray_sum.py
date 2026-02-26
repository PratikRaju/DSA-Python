arr=[-2,1,-3,4,-1,2,1,-5,4]
maxi=float("-inf")
n=len(arr)
total=0
for i in range(0,n):
    total=total+arr[i]
    maxi=max(maxi,total)
    if total<0:
        total=0
print(maxi)