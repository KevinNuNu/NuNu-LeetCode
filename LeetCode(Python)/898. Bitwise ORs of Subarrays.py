class Solution:
    def subarrayBitwiseORs1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 方法一：时间复杂度O(n^2), 72 / 83 个通过测试用例.
        # 用二维dp[i][j]保存i到j的subarray的计算结果
        # 状态转移公式为：dp[i][j] = dp[i][j-1] | A[j]
        n = len(A)
        dp = [[-1 for i in range(n)] for j in range(n)]
        # 将单独的一个元素放入数组
        for i in range(n):
            dp[i][i] = A[i]
        # 状态转移
        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = dp[i][j-1] | A[j]
        # 统计结果
        res = set()
        for i in range(n):
            res |= set(dp[i])
        # 去掉dp数组生成时产生的-1
        return len(res) - 1 if -1 in res else len(res)

    def subarrayBitwiseORs2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 方法二：时间复杂度O(32*n)
        # 因为二维dp数组实际还是有很多计算结果是重复的
        # 利用32位数字按位或运算的特性，当且仅当原本为"0"的位置出现"1"与之或运算后，才会变为"1"出现一个新的数
        # 也就是说最多最多当32位都位"1"时，任何数与之或运算都不会产生新的数
        # 即另dp[i]储存以A[i]结尾的subarray的结果，len(dp[i]) <= 32的，不再需要前面n那么大
        # 而dp[i]可以用一个滚动集合cur来实现
        cur = set()
        ans = set()
        for a in A:
            cur = {a | b for b in cur} | {a}
            ans |= cur
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.subarrayBitwiseORs2([1,2,4]))