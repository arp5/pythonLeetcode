class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        counter = {}
        n = len(s)
        max_window = 0
        for R in range(n):
            counter[s[R]] = 1+counter.get(s[R],0)
            if R-L+1-max(counter.values())>k:
                #shrink window
                counter[s[L]]-=1
                if counter[s[L]]==0:
                    counter.pop(s[L])
                L+=1
            max_window = max(max_window,R-L+1)
        return max_window
