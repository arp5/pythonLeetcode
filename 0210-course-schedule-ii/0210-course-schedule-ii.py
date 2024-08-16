class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        ans = []
        indegree = [0]*numCourses
        for i in range(numCourses):
            prereq[i] = []
        for course,pre in prerequisites:
            prereq[pre].append(course)
            indegree[course]+=1
        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            course = queue.pop(0)
            ans.append(course)
            for c in prereq[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        return ans if len(ans)==numCourses else []
#TC: O(N); SC: O(N)

        
