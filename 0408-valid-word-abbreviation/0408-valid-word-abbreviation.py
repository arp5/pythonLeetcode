class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr)>len(word):
            return False
        i,j=0,0
        curnum = 0
        while j<len(abbr):
            if abbr[j].isdigit():
                if curnum==0 and int(abbr[j])==0:
                    return False
                curnum = curnum*10+int(abbr[j])
                j+=1
            else:
                i+=curnum
                curnum=0
                print(i,j)
                if i<len(word) and j<len(abbr) and word[i]!=abbr[j]:
                    return False
                else:
                    i+=1
                    j+=1
        i+=curnum
        return i==len(word) and j==len(abbr)
            