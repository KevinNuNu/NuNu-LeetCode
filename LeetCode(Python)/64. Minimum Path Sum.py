class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        if n < 1 or m < 1:
            return None

        # 初始化第一列
        rows = [0 for _ in range(n)]
        rows[0] = grid[0][0]
        for i in range(1, n):
            rows[i] = rows[i-1] + grid[i][0]
        # 初始化第一行
        cols = [0 for _ in range(m)]
        cols[0] = grid[0][0]
        for j in range(1, m):
            cols[j] = cols[j-1] + grid[0][j]

        for i in range(1, n):
            cols[0] = rows[i]
            for j in range(1, m):
                # 取到达该点时的最短路程
                cols[j] = min(cols[j], cols[j-1]) + grid[i][j]

        return cols[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1]]))
