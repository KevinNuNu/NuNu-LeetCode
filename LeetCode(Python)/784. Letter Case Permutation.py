class Solution(object):
    def __init__(self):
        self.result = []

    def letterCasePermutation1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 递归解法
        n = len(S)
        letter_idx = []
        for idx, char in enumerate(S):
            if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                letter_idx.append(idx)

        def dfs(cur, cur_len):
            if cur_len == n:
                res = ''.join(cur)
                self.result.append(res)
                return

            if cur_len in letter_idx:
                cur.append(S[cur_len].upper())
                dfs(cur, cur_len+1)
                cur.pop()
                cur.append(S[cur_len].lower())
                dfs(cur, cur_len+1)
                cur.pop()
            else:
                cur.append(S[cur_len])
                dfs(cur, cur_len+1)
                cur.pop()

            return

        dfs([], 0)
        return self.result

    def letterCasePermutation2(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # 迭代解法
        result = []
        for idx, char in enumerate(S):
            if idx == 0:
                if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    result.extend([char.lower(), char.upper()])
                else:
                    result.append(char)
            else:
                if char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    add = []
                    for res in result:
                        add.extend([res + char.lower(), res + char.upper()])
                    result = add
                else:
                    result = [res + char for res in result]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation2('a1b2'))

