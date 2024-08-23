class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        pst,pend = intervals[0]
        n = len(intervals)
        count = 0
        for i in range(1,n):
            st,end = intervals[i]
            if st<pend:
                count+=1
            else:
                pst,pend = st,end
        return count