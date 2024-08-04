class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        openb,closeb = 0,0
        for c in s:
            if c=='(':
                openb+=1
                stack.append(c)
            elif c==')':
                if closeb<openb:
                    closeb+=1
                    stack.append(c)
            else:
                stack.append(c)
        ans = []
        while stack:
            c = stack.pop()
            if c==')':
                closeb-=1
                openb-=1
                ans.append(c)
            elif c=='(':
                if openb>closeb:
                    openb-=1
                else:
                   ans.append(c)
            else:
                ans.append(c)
        ans.reverse()
        return "".join(ans) 

                    