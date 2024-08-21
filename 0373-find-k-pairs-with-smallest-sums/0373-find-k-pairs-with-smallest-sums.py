class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i,j = 0,0
        n,m = len(nums1),len(nums2)
        visited = set()
        heap,ans = [],[]
        visited.add((i,j))
        heap.append((nums1[i]+nums2[j],i,j))
        while heap and len(ans)<k:
            x,y,z = heapq.heappop(heap)
            ans.append([nums1[y], nums2[z]])
            if y+1<n and (y+1,z) not in visited:
                visited.add((y+1,z))
                heapq.heappush(heap,(nums1[y+1]+nums2[z],y+1,z))
            if z+1<m and (y,z+1) not in visited:
                visited.add((y,z+1))
                heapq.heappush(heap,(nums2[z+1]+nums1[y],y,z+1))
        return ans
