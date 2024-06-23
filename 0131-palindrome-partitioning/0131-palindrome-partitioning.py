class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalindrome(s):
            return s==s[::-1]
        def bt(s,cur_comb):
            print(s,cur_comb)
            if not s:
                ans.append(cur_comb[:])
                return
            for i in range(1,len(s)+1):
                if isPalindrome(s[:i]):
                    cur_comb.append(s[:i])
                    bt(s[i:],cur_comb)
                    cur_comb.pop()
        bt(s,[])
        return ans