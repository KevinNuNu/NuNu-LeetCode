class Solution:
    def __init__(self):
        self.board = None
        self.candidate_number = None
        self.w = None
        self.h = None
        self.col = None
        self.row = None
        self.box = None
        self.col_res = None
        self.row_res = None
        self.box_res = None

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.candidate_number = set([str(i) for i in range(1, 10)])
        if self.board is None:
            return
        self.h = len(self.board)
        self.w = len(self.board[0])
        self.solver(0, -1)

    def solver(self, cur_y, last_x):
        # 判断是否搜索完所有行
        if cur_y == self.h:
            return True
        # 判断是否需要换行搜索
        if (last_x+1 == self.w) or ('.' not in self.board[cur_y][last_x+1:]):
            if self.solver(cur_y + 1, -1):
                return True

        for x in range(last_x+1, self.w):
            if self.board[cur_y][x] != '.':
                continue
            else:
                intersection = self.get_available_number(cur_y, x)
                if intersection == set():
                    # print('can\'t move on...')
                    return False
                else:
                    for put_number in intersection:
                        self.board[cur_y][x] = str(put_number)
                        # print('put {} in ({},{})'.format(put_number, cur_y, x))
                        if self.solver(cur_y, x):
                            return True
                        self.board[cur_y][x] = '.'
                        # print('remove {} in ({},{})'.format(put_number, cur_y, x))
                    if self.board[cur_y][x] == '.':
                        # print('can\'t move on...')
                        return False

    def get_available_number(self, y, x):
        # 初始化row,col,box,row_res,col_res,box_res
        self.row = set()
        self.col = set()
        self.box = set()
        self.col_res = set()
        self.row_res = set()
        self.box_res = set()

        # 得到row上已有数字
        for item in self.board[y]:
            if item != '.':
                self.row.add(item)
            else:
                continue
        # 得到col上已有数字
        for row in range(self.h):
            if self.board[row][x] != '.':
                self.col.add(self.board[row][x])
            else:
                continue
        # 得到box上已有数字
        box_x = x//3
        box_y = y//3
        if box_x == 0:
            box_x1 = 0
            box_x2 = 2
        elif box_x == 1:
            box_x1 = 3
            box_x2 = 5
        else:
            box_x1 = 6
            box_x2 = 8
        if box_y == 0:
            box_y1 = 0
            box_y2 = 2
        elif box_y == 1:
            box_y1 = 3
            box_y2 = 5
        else:
            box_y1 = 6
            box_y2 = 8
        for y in range(box_y1, box_y2+1):
            for x in range(box_x1, box_x2+1):
                if self.board[y][x] != '.':
                    self.box.add(self.board[y][x])
                else:
                    continue

        # 得到row,col,box上剩余可填数字集合
        self.row_res = self.candidate_number - self.row
        self.col_res = self.candidate_number - self.col
        self.box_res = self.candidate_number - self.box

        # 取三个集合的交集
        temp = self.row_res - (self.row_res - self.col_res)
        return temp - (temp - self.box_res)


if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku(
        [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]])
    )
