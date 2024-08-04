class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        curnum = 0
        for c in s:
            if c==" ":
                continue
            elif c.isdigit():
               curnum = curnum*10+int(c)
            else:
                if operator == '+':
                    stack.append(curnum)
                elif operator == '-':
                    stack.append(-curnum)
                elif operator == '*':
                    val = stack.pop()*curnum
                    stack.append(val)
                elif operator == '/':
                    num = stack.pop()
                    val = abs(num)//curnum
                    if num<0:
                        val*=-1
                    stack.append(val)
                operator = c
                curnum = 0
        if operator == '+':
            stack.append(curnum)
        elif operator == '-':
            stack.append(-curnum)
        elif operator == '*':
            val = stack.pop()*curnum
            stack.append(val)
        elif operator == '/':
            num = stack.pop()
            val = abs(num)//curnum
            if num<0:
                val*=-1
            stack.append(val)
        operator = c
        curnum = 0
        print(stack)
        ans = 0
        while stack:
            ans+=stack.pop(0)
        return ans