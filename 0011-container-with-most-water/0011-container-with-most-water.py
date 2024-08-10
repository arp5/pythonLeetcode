class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        amt,maxamt = 0,0
        start,end = 0,n-1
        while start<end:
            amt = min(height[start],height[end])*(end-start)
            maxamt = max(maxamt,amt)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return maxamt