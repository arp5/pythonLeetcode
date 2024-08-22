class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heap.append(intervals[0])
        n = len(intervals)
        ans = 0
        print(heap)
        for i in range(1,n):
            st,end = intervals[i]
            pst,pend = heapq.heappop(heap)
            if st<pend:
                #overlap
                ans+=1
                if pend<end:
                    heap.append((pst,pend))
                else:
                    heap.append((st,end))
            else:
                heapq.heappush(heap,(st,end))
        return ans

