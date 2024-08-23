class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if x<0:
            isNeg = True
            x=x*-1
        if x==0:
            return x
        ans = 0
        while x>0:
            ans = ans*10+(x%10)
            x = x//10
        if isNeg:
            ans = -1*ans
        if ans>pow(2,31)-1 or ans<-pow(2,31):
            return 0
        return ans
        
        