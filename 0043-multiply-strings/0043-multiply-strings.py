class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n,m = len(num1),len(num2)
        if m>=n:
            b = m
            nm2 = num2
            a = n
            nm1 = num1
        else:
            a = m
            nm2 = num1
            b = n
            nm1 = num2
        ans,c,u = 0,0,0
        cur,s1,s = 0,0,0
        for i in reversed(range(a)):
            n1 = nm1[i]
            count=0
            for j in reversed(range(b)):
                n2 = nm2[j]
                s1 = int(n2)*int(n1) + c
                s = s1%10
                c = s1//10
                cur = s*(pow(10,count))+cur
                count+=1
                print(cur)
            if c:
                cur = c*(pow(10,count))+cur
            cur = cur*pow(10,u)
            ans+=cur
            u+=1
            print("a",ans)
            cur=0
            c=0
        ansa = []
        if ans ==0:
            return "0"
        while ans>0:
            ansa.append(str(ans%10))
            ans=ans//10
        ansa.reverse()
        answer = "".join(ansa)
        return answer