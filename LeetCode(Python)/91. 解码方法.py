class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        if s[0] == '0':
            return 0

        # 初始化dp数组以及边界条件
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1

        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]
            
        return dp[n]