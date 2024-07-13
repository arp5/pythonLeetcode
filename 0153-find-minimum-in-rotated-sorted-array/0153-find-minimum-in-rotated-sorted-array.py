class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        res = float('inf')
        while start<=end:
            if nums[start]<nums[end]:
                res = min(res,nums[start])

            mid = (start+end)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[start]:
                start = mid+1
            else:
                end = mid
            if start==end:
                res = min(res,nums[start])
                return res
        return res