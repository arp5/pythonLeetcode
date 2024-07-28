class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        start = 1
        end = max(ribbons)
        def numk(val):
            ans=0
            for i in ribbons:
                ans+=(i//val)
            return ans
        while start<=end:
            mid = start+(end-start)//2
            numl = numk(mid)
            print(numl, start,end)
            if numl<k:
                end=mid-1
            else:
                start = mid+1
        return end

