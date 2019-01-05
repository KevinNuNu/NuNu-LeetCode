class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        res = []
        if N == 1:
            for i in range(10):
                res.append(i)
            return res

        def dfs(val, pre, pos):
            if pos == -1:
                res.append(val)
                return

            for i in range(10):
                if i == 0:
                    if pre == K:
                        dfs(val, 0, pos - 1)
                else:
                    if abs(i - pre) == K:
                        val += i * 10 ** pos
                        dfs(val, i, pos - 1)
                        val -= i * 10 ** pos

        for i in range(1, 10):
            val = 0
            val += i * 10 ** (N - 1)
            dfs(val, i, N - 2)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numsSameConsecDiff(3, 7))






