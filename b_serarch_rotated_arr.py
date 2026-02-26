class Solution:
    def sol(self,arr,target):
        n=len(arr)
        lb=0
        ub=n-1
        while lb<=ub:
            mid=(lb+ub)//2
            if arr[mid]==target:
                return mid
            if arr[mid]<=arr[ub]:
                if arr[mid]<=target<=arr[ub]:
                    lb=mid+1
                else:
                    ub=mid-1
            else:
                if arr[lb]<=target<=arr[mid]:
                    ub=mid-1
                else:
                    lb=mid+1
        return -1

arr=[10,11,12,13,1,2,3,4]
target=1
s=Solution()
tar=s.sol(arr,target)
print([tar])
    