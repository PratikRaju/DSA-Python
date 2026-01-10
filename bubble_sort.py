def bubble(num):
    n=len(num)
    is_swap=False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                is_swap=True
        if is_swap==False:
            break
    return num
arr=[1,2,3,4,5,6]
bubble_sort=bubble(arr)
print(bubble_sort)