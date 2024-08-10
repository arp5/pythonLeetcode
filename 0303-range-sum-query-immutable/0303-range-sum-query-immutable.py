class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefixsum = [0]*n
        self.prefixsum[0] = nums[0]
        for i in range(1,n):
            self.prefixsum[i]=nums[i]+self.prefixsum[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.prefixsum[right]-self.prefixsum[left-1]
        return self.prefixsum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)