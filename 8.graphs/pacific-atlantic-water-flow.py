from collections import deque


# Coordinates are (row, column) -> (y, x)

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0

        pacificQueue = deque()
        atlanticQueue = deque()

        for col in range(cols):
            pacificQueue.append((0, col))
            atlanticQueue.append((rows - 1, col))

        for row in range(rows):
            pacificQueue.append((row, 0))
            atlanticQueue.append((row, cols - 1))
        pacificVisited = self.bfs(pacificQueue, matrix)
        atlanticVisited = self.bfs(atlanticQueue, matrix)

        return pacificVisited.intersection(atlanticVisited)

    def bfs(self, queue, matrix):  # O(M * N)
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0

        visited = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            else:
                visited.add(current)
                for direction in directions:
                    dy, dx = direction
                    y, x = current[0] + dy, current[1] + dx
                    if 0 <= y < rows and 0 <= x < cols:
                        if matrix[y][x] >= matrix[current[0]][current[1]]:
                            queue.append((y, x))
        return visited