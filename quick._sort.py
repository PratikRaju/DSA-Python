def partition(num,low,high):
    i=low
    j=high
    pivot=num[i]
    while i<j:
        while num[i]<=pivot and i<=high-1:
            i+=1
        while num[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            num[i],num[j]=num[j],num[i]
    num[low],num[j]=num[j],num[low] 
    return j
def quick_sort(num,low,high):
    if low<high:
        p_index=partition(num,low,high)
        quick_sort(num,low,p_index-1)
        quick_sort(num,p_index+1,high)
arr=[4,3,1,2,7,6,8]
quick_sort(arr,0,len(arr)-1)
print(arr)