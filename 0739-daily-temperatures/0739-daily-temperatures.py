class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                x,t = stack.pop()
                ans[x] = i-x
            stack.append((i,temp))
        return ans