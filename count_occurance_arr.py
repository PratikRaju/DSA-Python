class Solution:
    def LowerBound(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        lb=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb
    def UpperBound(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        ub=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub
arr=[1,2,2,3,3,3,3,4,4,5,5,6,7,8,9]
sol=Solution()
lower=sol.LowerBound(arr,9)
upper=sol.UpperBound(arr,9)
print([upper-lower])
        