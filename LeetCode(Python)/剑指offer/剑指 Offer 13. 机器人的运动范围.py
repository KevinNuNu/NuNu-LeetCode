class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def cal(i):
            total = 0
            while i != 0:
                total += i % 10
                i //= 10
            return total

        def dfs(i, j, k, arr):
            if not 0 <= i < m or not 0 <= j < n or (cal(i) + cal(j)) > k or arr[i][j] == 1:
                return 0
            arr[i][j] = 1
            return 1 + dfs(i-1, j, k, arr) + dfs(i+1, j, k, arr) + dfs(i, j-1, k, arr) + dfs(i, j+1, k, arr)

        arr = [[0]*n for _ in range(m)]
        count = dfs(0, 0, k, arr)

        return count