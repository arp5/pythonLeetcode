class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        queue = []
        n,m = len(grid), len(grid[0])
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and not visited[i][j]:
                    islands+=1
                    queue.append((i,j))
                    visited[i][j] = True
                    while queue:
                        x,y = queue.pop(0)
                        if  x-1>=0 and grid[x-1][y] == "1" and not visited[x-1][y]:
                            queue.append((x-1,y))
                            visited[x-1][y] = True
                        if  x+1<n and grid[x+1][y] == "1" and not visited[x+1][y]:
                            queue.append((x+1,y))
                            visited[x+1][y] = True
                        if  y-1>=0 and grid[x][y-1] == "1" and not visited[x][y-1]:
                            queue.append((x,y-1))
                            visited[x][y-1] = True
                        if  y+1<m and grid[x][y+1] == "1" and not visited[x][y+1]:
                            queue.append((x,y+1))
                            visited[x][y+1] = True
        return islands