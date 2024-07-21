class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        seen = {}
        maxw = 0
        for R in range(len(s)):
            if s[R] in seen:
                L=max(seen[s[R]]+1,L)
            seen[s[R]] = R
            #print(L, seen)
            maxw = max(maxw, R-L+1)
        return maxw 
