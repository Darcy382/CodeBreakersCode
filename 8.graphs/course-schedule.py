from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        inVertecies = [0] * numCourses
        for prereq in prerequisites:
            inVertecies[prereq[0]] += 1
            adjList[prereq[1]].append(prereq[0])

        queue = deque()
        for course in range(numCourses):
            if inVertecies[course] == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            for neighbor in adjList[current]:
                inVertecies[neighbor] -= 1
                if inVertecies[neighbor] == 0:
                    queue.append(neighbor)

        for course in range(numCourses):
            if inVertecies[course]:
                return False
        return True
