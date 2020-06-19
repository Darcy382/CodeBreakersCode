import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        inEdges = [0] * numCourses
        order = []

        for prereq in prerequisites:
            adjList[prereq[1]].append(prereq[0])
            inEdges[prereq[0]] += 1

        queue = collections.deque()

        for course in range(numCourses):
            if inEdges[course] == 0:
                queue.append(course)

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in adjList[current]:
                inEdges[neighbor] -= 1
                if inEdges[neighbor] == 0:
                    queue.append(neighbor)
        if len(order) != numCourses:
            return []

        return order
