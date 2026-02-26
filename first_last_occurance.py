class Solution:
    def LowerBound(self,arr,target):
        n=len(arr)
        first=0
        last=n-1
        lb=-1
        while first<=last:
            mid=(first+last)//2
            if arr[mid]>=target:
                lb=mid
                last=mid-1
            else:
                first=mid+1
        return lb
    def UpperBound(self,arr,target):
        n=len(arr)
        first=0
        last=n-1
        ub=n
        while first<=last:
            mid=(first+last)//2
            if arr[mid]>target:
                ub=mid
                last=mid-1
            else:
                first=mid+1
        return ub

arr=[1,2,3,3,3,3,4,5,6,6,6,6,8,9]
sol=Solution()
low=sol.LowerBound(arr,9)
high=sol.UpperBound(arr,9)
print([low,high-1])

