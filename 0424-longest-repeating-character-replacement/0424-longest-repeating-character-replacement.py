class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L=0
        maxw = 0
        for R in range(len(s)):
            freq[s[R]] = 1+freq.get(s[R],0)
            if sum(freq.values())-max(freq.values())>k:
                freq[s[L]]-=1
                L+=1
            maxw = max(maxw,R-L+1)
        return maxw