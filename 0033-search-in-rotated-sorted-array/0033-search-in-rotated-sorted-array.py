class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[start]:
                if target<nums[mid] and target>=nums[start]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target>nums[mid] and target<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            if start==end:
                if target == nums[start]:
                    return start
                else:
                    return -1
        return -1