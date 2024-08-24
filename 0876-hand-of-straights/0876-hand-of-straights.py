class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        counter = Counter(hand)
        heap = list(counter.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            for i in range(first,groupSize+first):
                if i not in counter:
                    return False
                counter[i]-=1
                if counter[i]==0:
                    if i!=heap[0]:
                        return False
                    heapq.heappop(heap)
        return True
#TC:O(NlogN)+O(kN); SC: O(N)