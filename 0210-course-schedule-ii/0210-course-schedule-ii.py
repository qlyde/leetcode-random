class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sorting
        # Kahn's Algorithm
        # BFS from nodes with 0 indegree, decrement neighbour indegree (simulating deleting visited node)
        # if neighbour indegree is now 0, BFS it (add to queue, able to take that course)
        courseGraph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for [course, prereq] in prerequisites:
            courseGraph[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)

        ret = []
        visited = 0
        while q:
            n = q.popleft()
            visited += 1
            ret.append(n)

            for neighbour in courseGraph[n]:
                indegree[neighbour] -= 1
                if not indegree[neighbour]:
                    q.append(neighbour)

        return ret if visited == numCourses else []
