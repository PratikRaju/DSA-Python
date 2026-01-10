print("Check the number is Armstrong or not")
n=int(input("Enter the number:"))
num=n
total=0
count=len(str(num))
while num>0:
    rev=num%10
    total=total+(rev**count)
    num=num//10
if total==n:
    print("True")
else:
    print("False")
