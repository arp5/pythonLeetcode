class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sp = nums[0]
        fp = nums[0]
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]
            if sp==fp:
                break
        print(sp,fp)
        sp = nums[0]
        while sp!=fp:
            sp = nums[sp]
            fp = nums[fp]
        return sp