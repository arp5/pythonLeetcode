class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [(intervals[0][1], intervals[0][0])]
        count = 0
        for i in range(1,len(intervals)):
            pend,pst = heap[0]
            st,end = intervals[i]
            count = max(count,len(heap))
            if st>=pend:
                heapq.heappop(heap)
            heapq.heappush(heap,(end,st))
        count = max(count,len(heap))
        return count
