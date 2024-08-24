class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = {}
        for i,c in enumerate(s):
            counter[c] = i
        n = len(s)
        ans = []
        i=0
        print(counter)
        while i<n:
            length=0
            end = counter[s[i]]
            j=i
            print(end)
            while j<end:
                end = max(end,counter[s[j]])
                length+=1
                j+=1
            i=end+1
            ans.append(length+1)
        return ans

