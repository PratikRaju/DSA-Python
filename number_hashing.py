n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
# using hash_list
''' hash_list=[0]*11
for i in n:
    hash_list[i]+=1
for j in m:
    if j<0 or j>10:
        print(0)
    else:
        print(hash_list[j]) '''
# using hash_dict
hash_dict={}
for i in range(0,len(n)):
    hash_dict[n[i]]=hash_dict.get(n[i],0)+1
for j in m:
    print("The occurance of ",j," is ",hash_dict.get(j,0))
