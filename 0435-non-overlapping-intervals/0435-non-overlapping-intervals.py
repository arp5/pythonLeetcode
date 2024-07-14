class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        i,j=0,1
        count = 0
        start1,end1 = intervals[0]
        while j<n:
            start2,end2 = intervals[j]
            if start2>=end1:
                j+=1
                start1 = start2
                end1 = end2
            else:
                if end2 > end1:
                    #remove end2
                    j+=1
                else:
                    j+=1
                    start1 = start2
                    end1 = end2
                count+=1
        return count
                