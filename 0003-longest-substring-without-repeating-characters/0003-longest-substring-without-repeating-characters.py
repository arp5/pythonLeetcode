class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        L = 0
        windowmap = {}
        maxwindow = 0
        if len(s)==0:
            return 0
        for R in range(n):
            if s[R] not in windowmap or windowmap[s[R]]<L:
                windowmap[s[R]] = R
            else:
                maxwindow = max(maxwindow,R-L)
                L = max(L,windowmap[s[R]]+1)
                windowmap[s[R]] = R
        maxwindow = max(maxwindow,R-L+1)
        return maxwindow