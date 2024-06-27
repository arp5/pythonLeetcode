class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        stack = []
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b+a)
                if token == '-':
                    stack.append(b-a)
                if token == '*':
                    stack.append(b*a)
                if token == '/':
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack.pop()