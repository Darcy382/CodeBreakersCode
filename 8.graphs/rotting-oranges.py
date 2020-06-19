class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0]) if grid else 0

        # Preprocessing
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    grid[row][col] = (2, 0)
                else:
                    grid[row][col] = (grid[row][col], -1)

        # Starting the rotting cycle
        finished = False
        minute = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while not finished:
            finished = True  # Assum finished until changes
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col][0] == 2 and grid[row][col][1] != minute:
                        for direction in directions:
                            i, j = row + direction[0], col + direction[1]
                            if self.validCord((i, j), rows, cols):
                                if grid[i][j][0] == 1:
                                    grid[i][j] = (2, minute)
                                    finished = False
            minute += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col][0] == 1:
                    return -1
        return minute - 2

    def validCord(self, cord, rows, cols):
        if 0 <= cord[0] < rows and 0 <= cord[1] < cols:
            return True
        return False
