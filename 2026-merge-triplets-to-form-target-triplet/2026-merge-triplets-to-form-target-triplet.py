class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        cur = [-float('inf'), -float('inf'), -float('inf')]
        t1,t2,t3 = target
        for i in range(n):
            c1,c2,c3 = cur
            x,y,z = triplets[i]
            if x<=t1 and y<=t2 and z<=t3:
                cur = [max(x,c1), max(y,c2), max(z,c3)]
                if cur == target:
                    return True
        return cur==target