class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            start1,end1 = ans.pop()
            start2,end2 = intervals[i]
            if start2>end1:
                #no overlap
                ans.append((start1,end1))
                ans.append((start2,end2))
            else:
                ans.append((min(start1,start2),max(end1,end2)))
        return ans