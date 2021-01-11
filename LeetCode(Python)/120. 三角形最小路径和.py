class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 空间复杂度 O(n)的方法
        N = len(triangle)
        dp = [0 for _ in range(N)]

        # init dp array
        dp[0] = triangle[0][0]

        for i in range(1, N):
            for j in range(i+1)[::-1]:
                if j == i:
                    dp[j] = dp[j-1] + triangle[i][i]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][0]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
        
        return min(dp)