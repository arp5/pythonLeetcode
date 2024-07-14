class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        i,j=0,1
        count = 0
        while j<n:
            start1,end1 = intervals[i]
            start2,end2 = intervals[j]
            if start2>=end1:
                i+=1
                j+=1
            else:
                if end2 > end1:
                    #remove end2
                    intervals.pop(j)
                    n-=1
                else:
                    intervals.pop(i)
                    n-=1
                count+=1
        return count
                