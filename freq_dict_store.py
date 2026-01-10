dict={}
lst=[1,2,1,3,3,4,2,1,4,5,6,6,5,6]


# 1st approach
# for i in range(0,len(lst)):
#     if lst[i] in dict:
#         dict[lst[i]]=dict[lst[i]]+1
#     else:
#         dict[lst[i]]=1


# 2nd approach
for j in range(0,len(lst)):
    dict[lst[j]]=dict.get(lst[j],0)+1
print(dict)