from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverseAdjList = [[] for _ in range(len(graph))]
        outEdges = [0] * len(graph)

        for node in range(len(graph)):
            for neighbor in graph[node]:
                reverseAdjList[neighbor].append(node)
                outEdges[node] += 1

        queue = deque()

        for node in range(len(graph)):
            if outEdges[node] == 0:
                queue.append(node)

        while queue:
            current = queue.popleft()
            for node in reverseAdjList[current]:
                outEdges[node] -= 1
                if outEdges[node] == 0:
                    queue.append(node)
        output = []

        for node in range(len(graph)):
            if outEdges[node] == 0:
                output.append(node)

        return output
