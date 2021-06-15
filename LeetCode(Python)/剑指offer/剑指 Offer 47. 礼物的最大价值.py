class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 空间复杂度O(m)
        row = len(grid)
        col = len(grid[0])
        dp = [0] * col
        
        init_row = 0
        for j in range(col):
            init_row += grid[0][j]
            dp[j] = init_row

        for i in range(1, row):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, col):
                dp[j] = max(dp[j], dp[j-1]) + grid[i][j]
        
        return dp[col-1]

    def maxValue1(self, grid: List[List[int]]) -> int:
        # 空间复杂度O(mn)
        row = len(grid)
        col = len(grid[0])
        dp = [[0] * col for _ in range(row)]

        init_row = 0
        for j in range(col):
            init_row += grid[0][j]
            dp[0][j] = init_row
        init_col = 0
        for i in range(row):
            init_col += grid[i][0]
            dp[i][0] = init_col
        
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        
        return dp[row-1][col-1]