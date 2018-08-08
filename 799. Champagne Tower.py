class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        rows = query_row+1
        ct = [[0]*(i+1) for i in range(rows)]
        ct[0][0] = poured

        for row in range(rows):
            for glass in range(len(ct[row])):
                if ct[row][glass] > 1:
                    overflow = ct[row][glass] - 1
                    ct[row][glass] = 1
                else:
                    continue

                if row < query_row:
                    ct[row+1][glass] += overflow / 2
                    ct[row+1][glass+1] += overflow / 2

        return ct[query_row][query_glass]


if __name__ == '__main__':
    s = Solution()
    print(s.champagneTower(4, 2, 0))
