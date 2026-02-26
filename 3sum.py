arr=[-2,0,1,-2,2,-2,2,2,0,0]
arr.sort()
n=len(arr)
ans=[]
for i in range(0,n):
    if arr[i]==arr[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        total=arr[i]+arr[j]+arr[k]
        if total<0:
            j+=1
        elif total>0:
            k-=1
        else:
            temp=[arr[i],arr[j],arr[k]]
            ans.append(temp)
            j+=1
            k-=1
            while arr[j]==arr[j-1]:
                j+=1
            while arr[k]==arr[k+1]:
                k-=1
print(ans)