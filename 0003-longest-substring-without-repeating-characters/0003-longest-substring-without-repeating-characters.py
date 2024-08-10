class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cmap = {}
        l = 0
        maxlen = 0
        if n ==0:
            return 0
        for r in range(n):
            if s[r] not in cmap or cmap[s[r]]<l:
                cmap[s[r]] = r
            else:
                maxlen = max(maxlen,r-l)
                l = max(l,cmap[s[r]])+1
                cmap[s[r]] = r
        maxlen = max(maxlen,r-l+1)
        return maxlen 