# Rearrange the positive and negtive numbers respectively
arr=[-4,5,2,-4,-5,10]
n=len(arr)
result=[0]*n
posind,negind=0,1
for i in range(0,n):
    if arr[i]>0:
        result[posind]=arr[i]
        posind+=2
    else:
        result[negind]=arr[i]
        negind+=2
print(result)
