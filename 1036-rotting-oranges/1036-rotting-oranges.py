class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh = False
        n,m = len(grid), len(grid[0])
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                    visited[i][j] = True
                if grid[i][j] == 1:
                    fresh = True
        if not fresh:
            return 0
        ans = -1
        while queue:
            x,y,t = queue.pop(0)
            grid[x][y] = 2
            ans = t
            if x-1>=0 and grid[x-1][y] == 1 and not visited[x-1][y]:
                visited[x-1][y] = True
                queue.append((x-1,y,t+1))
            if x+1<n and grid[x+1][y] == 1 and not visited[x+1][y]:
                visited[x+1][y] = True
                queue.append((x+1,y,t+1))
            if y-1>=0 and grid[x][y-1] == 1 and not visited[x][y-1]:
                visited[x][y-1] = True
                queue.append((x,y-1,t+1))
            if y+1<m and grid[x][y+1] == 1 and not visited[x][y+1]:
                visited[x][y+1] = True
                queue.append((x,y+1,t+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return ans
            