class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [(intervals[0])]
        n = len(intervals)
        for i in range(1,n):
            st1,end1 = ans.pop()
            st2,end2 = intervals[i]
            if st2>end1:
                #no overlap
                ans.append((st1,end1))
                ans.append((st2,end2))
            elif st2<=end1:

                ans.append((st1,max(end1,end2)))
        return ans 