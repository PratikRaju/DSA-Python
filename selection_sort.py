def sort_arr(arr):
    n=len(arr)
    for i in range(0,n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    return arr
my_arr=[5,1,2,7,6]
sorted_arr=sort_arr(my_arr)
print(sorted_arr)