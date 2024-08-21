class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = Counter(s1)
        k,n = len(s1),len(s2)
        s2map = {}
        L=0
        if n<k:
            return False
        for R in range(k):
            s2map[s2[R]] = 1+s2map.get(s2[R],0)
        if s2map == s1map:
            return True
        for R in range(k,n):
            s2map[s2[R]] = 1+s2map.get(s2[R],0)
            s2map[s2[L]]-=1
            if s2map[s2[L]]==0:
                s2map.pop(s2[L])
            L+=1
            if s2map == s1map:
                return True
        return False