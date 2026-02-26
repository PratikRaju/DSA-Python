arr=[1,1,1,1,2,2,3,3,3,4,4,4,5,5]
target=8
arr.sort()
n=len(arr)
ans=[]
for i in range(0,n):
    if i>0 and arr[i]==arr[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and arr[j]==arr[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            total=arr[i]+arr[j]+arr[k]+arr[l]
            if total==target:
                temp=[arr[i],arr[j],arr[k],arr[l]]
                ans.append(temp)
                k+=1
                l-=1
                while arr[k]==arr[k-1]:
                    k+=1
                while arr[l]==arr[l+1]:
                    l-=1
            elif total<target:
                k+=1
            else:
                l-=1
print(ans)
        
                    
    