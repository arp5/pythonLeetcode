class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start,end = 0,n-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            #if left is sorted
            if nums[start]<=nums[mid]:
                if target<nums[start] or target>nums[mid]:
                    start=mid+1
                else:
                    end = mid-1
            else:
                if target<nums[mid] or target>nums[end]:
                    end = mid-1
                else:
                    start = mid+1
        return -1