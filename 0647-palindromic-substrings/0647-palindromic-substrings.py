class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            #odd substrings
            j,k = i,i
            while j>=0 and k<n and s[j]==s[k]:
                count+=1
                j-=1
                k+=1
            #even substrings
            j,k = i,i+1
            while j>=0 and k<n and s[j]==s[k]:
                count+=1
                j-=1
                k+=1
        return count