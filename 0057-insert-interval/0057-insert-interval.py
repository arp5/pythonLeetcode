class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        start,end = newInterval
        if start<=intervals[0][0]:
            intervals.insert(0,newInterval)
        i=0
        while i<len(intervals) and start>intervals[i][0]:
            i+=1
        intervals.insert(i,newInterval)
        print(intervals)
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1,n):
            print(ans)
            st1,end1 = ans.pop()
            st2,end2 = intervals[i]
            if st2>end1:
                ans.append((st1,end1))
                ans.append((st2,end2))
            else:
                ans.append((st1, max(end1,end2)))
        return ans