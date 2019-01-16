class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if n < 1 or m < 1 or obstacleGrid[0][0] == 1:
            return 0

        # 由于只能向右和向下，所以第一行第一列出现阻挡，后面都不可能到达
        rows = [0 for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] != 1:
                rows[i] = 1
            else:
                break
        cols = [0 for _ in range(m)]
        for j in range(m):
            if obstacleGrid[0][j] != 1:
                cols[j] = 1
            else:
                break

        for i in range(1, n):
            # 将第一列的状态赋给cols[0]（不再一直是1了）
            cols[0] = rows[i]
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    cols[j] = cols[j] + cols[j-1]
                else:
                    # 该位置出现阻挡，则从该点出发的可能路线即为0
                    cols[j] = 0

        return cols[-1]
