class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        stack = []
        getColor = [1, 0]
        for i in range(len(graph)):
            if i not in colors:
                colors[i] = 1
                stack.append(i)
                while stack:
                    current = stack.pop()
                    for neighbor in graph[current]:
                        if neighbor in colors:
                            if colors[neighbor] == colors[current]:
                                return False
                        else:
                            colors[neighbor] = getColor[colors[current]]
                            stack.append(neighbor)
        return True