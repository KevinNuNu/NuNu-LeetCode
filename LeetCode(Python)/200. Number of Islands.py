class Solution:
    def __init__(self):
        self.grid = None
        self.h = None
        self.w = None
        self.num = None

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid:
            self.grid = grid
            self.h = len(grid)
            self.w = len(grid[0])
            self.num = 0
            for i in range(self.h):
                for j in range(self.w):
                    if self.grid[i][j] == '1':
                        self.num += 1
                        self.dfs(i, j)
            return self.num
        else:
            return 0

    def dfs(self, i, j):
        if 0 <= i < self.h and 0 <= j < self.w and self.grid[i][j] == '1':
            self.grid[i][j] = '0'
            self.dfs(i-1, j)
            self.dfs(i+1, j)
            self.dfs(i, j-1)
            self.dfs(i, j+1)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
