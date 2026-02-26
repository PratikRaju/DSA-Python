s_price=[7,6,5,4,3,2]
n=len(s_price)
maxi=0
for i in range(0,n):
    for j in range(i+1,n):
        if s_price[i]<s_price[j]:
            diff=s_price[j]-s_price[i]
            maxi=max(maxi,diff)
print(maxi)

