class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return None

        def dfs(string, left, right, res):
            if left == n:
                res.append(string + ')' * (n - right))
                return

            if right > left:
                return

            dfs(string + '(', left + 1, right, res)
            dfs(string + ')', left, right + 1, res)

        result = []
        dfs('', 0, 0, result)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(4))
