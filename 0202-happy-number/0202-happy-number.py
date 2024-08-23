class Solution:
    def isHappy(self, n: int) -> bool:
        def getsq(n):
            sq = 0
            while n>0:
                sq += (n%10)*(n%10)
                n = n//10
            return sq
        sp,fp = n,n
        while fp!=1:
            sp = getsq(sp)
            fp = getsq(getsq(fp))
            if sp!=1 and sp==fp:
                return False
        return True