def palindrom():
    name=input("Enter your name:").lower()
    left=0
    right=len(name)-1
    while left<right:
        if name[left]!=name[right]:
            return False
        left+=1
        right-=1
    return True
print(palindrom())