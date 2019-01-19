class Solution:
    def stoneGame1(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # min-max解法，不带记忆数组，此时有很多重复计算部分，时间复杂度为O(2^n)
        n = len(piles)

        def score(p, l, r):
            if l == r:
                return p[l]

            return max(p[l] - score(p, l+1, r), p[r] - score(p, l, r-1))

        return score(piles, 0, n-1) > 0

    def stoneGame2(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # min-max解法，带记忆数组，递归解法，时间复杂度为O(n^2)，空间复杂度为O(n^2)，容易stack overflow
        n = len(piles)
        tag_array = [[-1 for j in range(n)] for i in range(n)]

        def score(p, l, r):
            if l == r:
                return p[l]

            # 判断从i到j的分数是否计算过
            if tag_array[l][r] == -1:
                tag_array[l][r] = max(p[l] - score(p, l + 1, r), p[r] - score(p, l, r - 1))

            return tag_array[l][r]

        return score(piles, 0, n - 1) > 0

    def stoneGame3(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # 二维数组dp的方法

        n = len(piles)
        # 初始化dp[i][j]数组，表示从i到j的最优选择
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        # 从最小的子问题开始，也就是长度为l时的情况
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        return dp[0][n-1] > 0

    def stoneGame4(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        # 滚动数组的dp方法
        # 因为dp数组实际仅和i和l有关，与j无关，所以是可以压缩到只和i有关的一维dp

        n = len(piles)
        # 初始化dp[i][j]数组，表示从i到j的最优选择
        dp = [piles[i] for i in range(n)]

        # 先从l=2开始，即从i=0开始，把(0,1)(1,2)...(n-2,n-1)的最优解保存
        # 再l=3，此时dp[0]表示的是从0开始，长度为3，即(0,1,2)的最优
        # 而(0,1,2)情况中，有个从1开始长度为2的最优情况即为dp[1]
        # (此时i指针仅到0，还未更新dp[1]，所以此时的dp[1]代表的还是从1开始长度为2的情况)
        for l in range(2, n+1):
            # dp[i]表示，从i开始，长度为l的情况中最优的选择
            for i in range(n-l+1):
                dp[i] = max(piles[i] - dp[i+1], piles[i+l-1] - dp[i])
        return dp[0] > 0
