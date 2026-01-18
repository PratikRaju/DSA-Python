def merge_array(left,right):
    i,j=0,0
    n,m=len(left),len(right)
    result=[]
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
            
        else:
            result.append(right[j])
            j+=1
    if i<n:
       while i<n:
           result.append(left[i])
           i+=1
    if j<m:
        while j<m:
           result.append(right[j])
           j+=1
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left_m=merge_sort(left_arr)
    right_m=merge_sort(right_arr)
    return merge_array(left_m,right_m)

unsort_arr=[2,4,2,5,6,78,5,23,26,7]
sort_arr=merge_sort(unsort_arr)
print(sort_arr)