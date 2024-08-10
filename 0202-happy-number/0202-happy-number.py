class Solution:
    def isHappy(self, n: int) -> bool:
        def sqsum(n):
            sqs = 0
            while n:
                r = n%10
                sqs+=(r*r)
                n=n//10
            return sqs
        n1 = sqsum(n)
        n2 = sqsum(n1)
        print(n1,n2)
        while n1!=1:
            print(n1,n2)
            if n1==n2:
                return False
            n1 = sqsum(n1)
            n2 = sqsum(sqsum(n2))
        return True