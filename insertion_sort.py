def insert(num):
    n=len(num)
    for i in range(1,n):
        key=num[i]
        j=i-1
        while j>=0 and num[j]>key:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
    return num
arr=[3,5,6,4,8,9,10,7,1]
insertion_sort=insert(arr)
print(insertion_sort)

        
