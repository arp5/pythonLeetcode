class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pset,aset = set(),set()
        queue = []
        n,m = len(heights), len(heights[0])
        for i in range(n):
            queue.append((i,0))
            pset.add((i,0))
        for j in range(1,m):
            queue.append((0,j))
            pset.add((0,j))
        visited = set()
        while queue:
            x,y = queue.pop(0)
            if x-1>=0 and heights[x-1][y]>=heights[x][y] and (x-1,y) not in visited:
                visited.add((x-1,y))
                queue.append((x-1,y))
                pset.add((x-1,y))
            if x+1<n and heights[x+1][y]>=heights[x][y] and (x+1,y) not in visited:
                visited.add((x+1,y))
                queue.append((x+1,y))
                pset.add((x+1,y))
            if y-1>=0 and heights[x][y-1]>=heights[x][y] and (x,y-1) not in visited:
                visited.add((x,y-1))
                queue.append((x,y-1))
                pset.add((x,y-1))
            if y+1<m and heights[x][y+1]>=heights[x][y] and (x,y+1) not in visited:
                visited.add((x,y+1))
                queue.append((x,y+1))
                pset.add((x,y+1))
        print(pset)
        for i in range(n):
            queue.append((i,m-1))
            aset.add((i,m-1))
        for j in range(m-1):
            queue.append((n-1,j))
            aset.add((n-1,j))
        visited = set()
        while queue:
            x,y = queue.pop(0)
            if x-1>=0 and heights[x-1][y]>=heights[x][y] and (x-1,y) not in visited:
                visited.add((x-1,y))
                queue.append((x-1,y))
                aset.add((x-1,y))
            if x+1<n and heights[x+1][y]>=heights[x][y] and (x+1,y) not in visited:
                visited.add((x+1,y))
                queue.append((x+1,y))
                aset.add((x+1,y))
            if y-1>=0 and heights[x][y-1]>=heights[x][y] and (x,y-1) not in visited:
                visited.add((x,y-1))
                queue.append((x,y-1))
                aset.add((x,y-1))
            if y+1<m and heights[x][y+1]>=heights[x][y] and (x,y+1) not in visited:
                visited.add((x,y+1))
                queue.append((x,y+1))
                aset.add((x,y+1))
        print(aset)
        return pset.intersection(aset)
