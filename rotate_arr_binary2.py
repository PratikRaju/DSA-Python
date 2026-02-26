class Solution:
    def sol(self,arr,target):
        n=len(arr)
        lb=0
        ub=n-1
        while lb<=ub:
            mid=(lb+ub)//2
            if arr[mid]==target:
                return True
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
        return False
arr=[11,12,13,14,1,2,3]
target=2
ans=Solution()
find=ans.sol(arr,target)
print(find)