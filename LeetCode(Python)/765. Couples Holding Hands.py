class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        if row:
            res = 0
            cp_dict = {}
            for i in range(0, len(row), 2):
                cp_dict[row[i]] = row[i+1]
                cp_dict[row[i+1]] = row[i]
            for i in range(0, len(row), 2):
                if cp_dict[i] != i+1:
                    left = cp_dict[i]
                    right = cp_dict[i+1]
                    cp_dict[left] = cp_dict[i+1]
                    cp_dict[right] = cp_dict[i]
                    res += 1
            return res
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSwapsCouples([0, 2, 1, 3]))

