# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 12:39:51 2018

@author: wzc118
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.rows_ = [[False for _ in range(10)] for _ in range(9)]
        self.cols_ = [[False for _ in range(10)] for _ in range(9)]
        self.boxes_ = [[False for _ in range(10)] for _ in range(9)]
                
        # initialization
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    self.rows_[i][n] = True
                    self.cols_[j][n] = True
                    self.boxes_[(i//3)*3+(j//3)][n] = True
        
        self.fill(board,0,0)
                    
    def fill(self,board,x,y):
        # x column, y row
        if y == 9:
            return True
        
        # nextx, nexty
        nx = (x+1)%9
        ny = (y+1) if (nx==0) else y
        
        if board[y][x] != '.':
            return self.fill(board,nx,ny)
        
        for i in range(1,10):
            k = '123456789'
            if not self.rows_[y][i] and not self.cols_[x][i] and not self.boxes_[(y//3)*3 + (x//3)][i]:
                self.rows_[y][i] = True
                self.cols_[x][i] = True
                self.boxes_[(y//3)*3 + (x//3)][i] = True
                board[y][x] = k[i-1]
                if self.fill(board,nx,ny):
                    return True
                board[y][x] = '.'
                self.rows_[y][i] = False
                self.cols_[x][i] = False
                self.boxes_[(y//3)*3 + (x//3)][i] = False
        return False