class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            target = -nums[i]
            j,k = i+1,n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while j<k:
                sumk = nums[j]+nums[k]
                if sumk == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<n and nums[j]==nums[j-1]:
                        j+=1
                elif sumk<target:
                    j+=1
                else:
                    k-=1
        return ans