class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        def dfs(x,y,k):
            if k==len(word):
                return True
            if x-1>=0 and board[x-1][y] == word[k] and not visited[x-1][y]:
                visited[x-1][y] = True
                if dfs(x-1,y,k+1):
                    return True
                visited[x-1][y] = False
            if x+1<n and board[x+1][y] == word[k] and not visited[x+1][y]:
                visited[x+1][y] = True
                if dfs(x+1,y,k+1):
                    return True
                visited[x+1][y] = False
            if y-1>=0 and board[x][y-1] == word[k] and not visited[x][y-1]:
                visited[x][y-1] = True
                if dfs(x,y-1,k+1):
                    return True
                visited[x][y-1] = False
            if y+1<m and board[x][y+1] == word[k] and not visited[x][y+1]:
                visited[x][y+1] = True
                if dfs(x,y+1,k+1):
                    return True
                visited[x][y+1] = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = [[False for j in range(m)] for i in range(n)]
                    visited[i][j] = True
                    if dfs(i,j,1):
                        return True
        return False