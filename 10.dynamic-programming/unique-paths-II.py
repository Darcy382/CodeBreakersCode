class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        0 0 0 1
        0 0 0 1
        1 1 1 1

        4 1
        2 1
        1 1

        '''
        if obstacleGrid is None:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0]) if obstacleGrid else 0
        if n <= 0:
            return 0
        elif m <= 0:
            return 0
        dp = [[-1] * m for _ in range(n)]

        if obstacleGrid[-1][-1] == 1:
            return 0
        else:
            dp[-1][-1] = 1

        for i in range(m - 2, -1, -1):
            if obstacleGrid[n - 1][i] == 0:
                dp[n - 1][i] = dp[n - 1][i + 1]
            else:
                dp[n - 1][i] = 0

        for i in range(n - 2, -1, -1):
            if obstacleGrid[i][m - 1] == 0:
                dp[i][m - 1] = dp[i + 1][m - 1]
            else:
                dp[i][m - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                else:
                    dp[i][j] = 0

        return dp[0][0]


