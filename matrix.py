arr=[[5,20,3],[7,10,9],[1,-52,6]]
row=len(arr)
col=len(arr[0])
total=0
result=[[0]*row for i in range(col)]
#---add the all element in the array
# for i in range(0,row):
#     for j in range(0,col):
#         total+=arr[i][j]
# print(total)
#---print upper triangle of the matrix
# for i in range(0,row):
#     for j in range(0,col):
#         if j>=i:
#             print(arr[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
#---print lower triangle of the matrix
# for i in range(0,row):
#     for j in range(0,col):
#         if j<=i:
#             print(arr[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
#---print diagonal of the matrix
# for i in range(0,row):
#     for j in range(0,col):
#         if j==i:
#             print(arr[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
#---print opposite diagonal of the matrix
# for i in range(0,row):
#     for j in range(0,col):
#         if i+j==2:
#             print(arr[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
#---Transpose of an matrix
for i in range(0,row):
    for j in range(0,col):
        result[j][i]=arr[i][j]
print(result)