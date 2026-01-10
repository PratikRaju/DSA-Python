# head recursion
def num(i,n):
    if n==0:
        return
    print(i)
    num(i+1,n-1)
num(1,5)
# tail recursion
def num(i,n):
    if n==5:
        return
    num(i-1,n+1)
    print(i)
num(5,0)
#print sum 1 to 10
def fun(sum,i,n):
    if i>n:
        print(sum)
        return
    fun(sum+i,i+1,n)
fun(0,1,10)