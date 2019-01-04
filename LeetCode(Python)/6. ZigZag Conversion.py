class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= 0 or numRows <= 0:
            return None

        if numRows == 1:
            return s

        res = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = 0
                while i + 2 * j * (numRows - 1) < length:
                    res += s[i + 2 * j * (numRows - 1)]
                    j += 1
            else:
                j = 0
                while 1:
                    one = i + 2 * j * (numRows - 1)
                    if one < length:
                        res += s[one]
                    else:
                        break
                    j += 1
                    two = one + 2 * (numRows - i - 1)
                    if two < length:
                        res += s[two]
                    else:
                        break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.convert(s="A", numRows=1))
    # print(s.convert(s = "PAYPALISHIRING", numRows = 3))3