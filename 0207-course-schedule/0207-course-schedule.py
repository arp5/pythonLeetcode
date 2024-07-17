class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        indegree = [0]*numCourses
        for i in range(numCourses):
            adjList[i] = []
        for c1,c2 in prerequisites:
            adjList[c2].append(c1)
            indegree[c1]+=1
        queue = []
        visited = set()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            course = queue.pop(0)
            visited.add(course)
            for c in adjList[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        return len(visited)==numCourses