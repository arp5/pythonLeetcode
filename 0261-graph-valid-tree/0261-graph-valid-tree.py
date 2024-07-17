class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        prev = -1
        visited = set()
        def dfs(node,prev):
            #base
            if node in visited:
                return False
            visited.add(node)
            for n in adjList[node]:
                if n==prev:
                    continue
                else:
                    if not dfs(n,node):
                        return False
            return True
        return dfs(0,-1) and len(visited)==n

