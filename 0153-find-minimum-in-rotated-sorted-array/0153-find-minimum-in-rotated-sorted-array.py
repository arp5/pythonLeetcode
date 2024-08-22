class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start,end = 0,n-1
        minnum = float('inf')
        while start<=end:
            mid = (start+end)//2
            minnum = min(minnum,nums[mid])
            if nums[start]<nums[end]:
                minnum = min(minnum,nums[start])
            if nums[start]<=nums[mid]:
                minnum = min(minnum,nums[start])
                start = mid+1
            else:
                end=mid-1
        return minnum
