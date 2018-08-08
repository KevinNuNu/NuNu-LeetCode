class Solution:
    def __init__(self):
        self.digits = None
        self.length = None
        self.num_dict = None
        self.ans = None

    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        self.length = len(digits)
        if self.length == 0:
            return []
        self.num_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.ans = []

        self.dfs(0, '')
        return self.ans

    def dfs(self, dig_length, cur):
        if dig_length == self.length:
            self.ans.append(cur)
            return

        key = self.digits[dig_length]
        cur_char = self.num_dict[key]
        for char in cur_char:
            cur = cur + char
            self.dfs(dig_length+1, cur)
            cur = cur[:-1]

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        self.length = len(digits)
        if self.length == 0:
            return []
        self.num_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        self.ans = ['']

        self.bfs()
        return self.ans

    def bfs(self):
        for key in self.digits:
            self.ans = [prefix + postfix for prefix in self.ans for postfix in self.num_dict[key]]


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations2('23'))
