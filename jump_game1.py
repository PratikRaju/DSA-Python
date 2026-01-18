def jump_num(num):
    max_ind=0
    for i in range(0,len(num)):
        if i>max_ind:
            return False
        max_ind=max(max_ind,i+num[i])
    return True
num=[1,2,1,2,0,4]
print(jump_num(num))