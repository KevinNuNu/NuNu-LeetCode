class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])

        N = [[0.5] + i + [0.5] for i in M]
        N = [[0.5] * (m + 2)] + N + [[0.5] * (m + 2)]

        A = []
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                A.append(N[i - 1][j - 1:j + 2] + N[i][j - 1:j + 2] + N[i + 1][j - 1:j + 2])

        for i in range(n * m):
            sum, count = 0, 0
            for j in range(9):
                if A[i][j] != 0.5:
                    sum += A[i][j]
                    count += 1
            M[i // m][i % m] = sum // count

        return M


if __name__ == '__main__':
    s = Solution()
    print(s.imageSmoother([[2,3,4],
                           [5,6,7],
                           [8,9,10],
                           [11,12,13],
                           [14,15,16]]))
