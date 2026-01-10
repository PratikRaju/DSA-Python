s="azyxyyzaaaa"
q=["d","a","y","x"]
# by list
hash_list=[0]*26
for i in s:
    ascii_val=ord(i)
    index=ascii_val-97
    hash_list[index]+=1
for j in q:
    ascii_val=ord(j)
    index=ascii_val-97
    print(hash_list[index])  
