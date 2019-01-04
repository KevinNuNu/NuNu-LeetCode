class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        f1 = 1
        f2 = 2
        t = 3
        while t <= n:
            f1, f2 = f2, f1 + f2
            t += 1

        return f2
