# 1d array
num=int(input("how many number you want to store in array?:"))
arr=[]
print("Enter",num,"element for your array:")
for i in range(num):
    element=input()
    arr.append(element)
print("\nThe array elements are")
print("[",end="")
for i in range(num):
    print(arr[i],end="")
    if i < num - 1:  # If it's not the last element
        print(",", end='')  # Print a comma
print("]")