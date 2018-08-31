class Solution:
    def __init__(self):
        self.board = None
        self.h = None
        self.w = None

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            self.board = board
            self.h = len(board)
            self.w = len(board[0])
            for j in range(self.w):
                if self.board[0][j] == 'O':
                    self.dfs(0, j)
                if self.board[-1][j] == 'O':
                    self.dfs(self.h-1, j)
            for i in range(self.h):
                if self.board[i][0] == 'O':
                    self.dfs(i, 0)
                if self.board[i][self.w-1] == 'O':
                    self.dfs(i, self.w-1)
            for i in range(self.h):
                for j in range(self.w):
                    if self.board[i][j] == 'O':
                        self.board[i][j] = 'X'
                    elif self.board[i][j] == -1:
                        self.board[i][j] = 'O'

    def dfs(self, i, j):
        if 0 <= i < self.h and 0 <= j < self.w and self.board[i][j] == 'O':
            self.board[i][j] = -1
            self.dfs(i-1, j)
            self.dfs(i+1, j)
            self.dfs(i, j-1)
            self.dfs(i, j+1)


if __name__ == '__main__':
    s = Solution()
    print(s.solve([["X","X","X","X"],
                   ["X","O","O","X"],
                   ["X","X","O","X"],
                   ["X","O","X","X"]]))
