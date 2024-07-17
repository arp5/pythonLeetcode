class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adjList = {}
        indegree = [0]*numCourses
        for i in range(numCourses):
            adjList[i] = []
        for c1,c2 in prerequisites:
            adjList[c2].append(c1)
            indegree[c1]+=1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop(0)
            ans.append(course)
            for c in adjList[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        return ans if len(ans)==numCourses else []