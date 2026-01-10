count=0
# head recursion
'''def greet():
    global count
    if count==4:
        return
    print("Raj")
    count+=1
    greet()
greet()'''
# tail recursion
def greet():
    global count
    if count==4:
        return
    count+=1
    greet()
    print("Raj")
greet()