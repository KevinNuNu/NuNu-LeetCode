class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        str_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        if n == 1:
            return str_dict.get(s[0])

        index = 0
        res = 0
        while index < n:
            if str_dict.get(s[index:index+2], None) is None:
                res += str_dict[s[index]]
                index += 1
            else:
                res += str_dict[s[index:index+2]]
                index += 2

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))