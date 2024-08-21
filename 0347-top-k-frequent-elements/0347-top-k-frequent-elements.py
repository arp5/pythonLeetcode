class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap,ans = [],[]
        for num,f in freq.items():
            heapq.heappush(heap,(f,num))
            if len(heap)>k:
                heapq.heappop(heap)
        while heap:
            ans.append(heap.pop()[1])
        return ans
#TC: O(Nlogk); SC: O(K)
