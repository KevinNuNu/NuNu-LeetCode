from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        # 初始化右上角元素
        row, col = 0, cols-1

        while (row < rows) and (col >= 0):
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                col -= 1
            
            if matrix[row][col] < target:
                row += 1
            
        return False    

