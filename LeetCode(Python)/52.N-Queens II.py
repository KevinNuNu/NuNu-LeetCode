class Solution:
    def __init__(self):
        self.board = None
        self.cols = None
        self.diag1 = None
        self.diag2 = None
        self.result = None

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.board = [['.'] * n for _ in range(n)]
        self.cols = [False] * n
        self.diag1 = [False] * (2*n-1)
        self.diag2 = [False] * (2*n-1)
        self.result = 0

        self.nqueens(n, 0)
        return self.result

    def available(self, x, y, n):
        return (not self.cols[x]) and (not self.diag1[x+y]) and (not self.diag2[x-y+n-1])

    def updateBoard(self, x, y, n, is_put):
        self.cols[x] = is_put
        self.diag1[x+y] = is_put
        self.diag2[x-y+n-1] = is_put
        self.board[y][x] = 'Q' if is_put else '.'

    def nqueens(self, n, y):
        if y == n:
            self.result += 1
            return

        for x in range(n):
            if not self.available(x, y, n):
                continue
            else:
                self.updateBoard(x, y, n, True)
                self.nqueens(n, y+1)
                self.updateBoard(x, y, n, False)


if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(5))
