class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        times = 0
        i,j=0,0
        while i<len(abbr):
            if abbr[i].isdigit():
                if times==0 and int(abbr[i])==0:
                    return False
                times=times*10+int(abbr[i])
            else:
                j+=times
                times = 0
                if j==len(word) and i==len(abbr):
                    return True
                elif j>=len(word) or i>=len(abbr):
                    return False
                if abbr[i]!=word[j]:
                    return False
                else:
                    j+=1
            i+=1
        j+=times
        return j==len(word) and i==len(abbr)
                