class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cols = [1 for _ in range(m)]

        for i in range(1, n):
            for j in range(1, m):
                cols[j] = cols[j] + cols[j-1]

        return cols[-1]
