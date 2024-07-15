class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for c1,c2 in prerequisites:
            adjList[c2].append(c1)
            indegree[c1]+=1
        queue = []
        visited = 0
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            c = queue.pop(0)
            visited+=1
            for n in adjList[c]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        return visited==numCourses