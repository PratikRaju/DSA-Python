#Dynamic Array
#1. Create List [D], #2. Len[D], #3. Append, #4. Print, #5. Indexing, #6. Pop, #7. Clear, #8. Find, #9. Insert, #10. Delete, #11. Remove
import ctypes
class meralist:
    def __init__(self):
        self.size=1 #how many items i can store in arrau
        self.n=0 # how many number the array have
        # create a c type array with size self.size
        self.A= self.__make_array(self.size)
    #length
    def __len__(self):
        return self.n
    #print
    def __str__(self):
        result=''
        for i in range(self.n):
            result=result+str(self.A[i])+','
        return '['+result[:-1]+']'
    #append
    def append(self,item):
        if self.size==self.n:
            #resize
            self.__resize(self.size*2)
        #append
        self.A[self.n]=item
        self.n=self.n+1
    def __resize(self,new_capacity):
        #create a new array with new capacity
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        #copy the content from A to B
        for i in range(self.n):
            B[i]=self.A[i]
        #reasign A
        self.A=B
    def __make_array(self,capacity):
        #creates a c type array with size capacity
        return (capacity*ctypes.py_object)()
L=meralist()
L.append('Hello')
L.append(3.4)
L.append(True)
L.append(100)
L.append(10.2)
print(L[0])