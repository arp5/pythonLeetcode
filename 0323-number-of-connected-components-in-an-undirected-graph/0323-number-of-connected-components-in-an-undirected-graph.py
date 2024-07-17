class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        queue = []
        visited= set()
        comp = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue.append(i)
                comp+=1
                while queue:
                    node = queue.pop(0)
                    for n in adjList[node]:
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)
        return comp
