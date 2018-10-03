class Solution1:
    """
    中心扩展法，时间复杂度为O(n^2)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        t = self.preprocess(s)
        n = len(t)
        p = [0 for _ in range(n)]
        for k in range(1, n-1):
            count = 0
            i = j = k
            while i >= 1 and j <= n-2:
                if t[i-1] == t[j+1]:
                    count += 1
                    i -= 1
                    j += 1
                else:
                    break
            p[k] = count

        length = max(p)
        t_index = p.index(length)
        res = t[t_index-length+1:t_index+length]

        return ''.join(res.split('#'))

    def preprocess(self, s):
        n = len(s)
        res = ''
        for i in range(n):
            res += '#' + s[i]
        res += '#'
        return res


class Solution2:
    # 中心扩展法的改进版，用到了当前最长回文字符串的对称性，减少不必要的计算。时间复杂度O(n)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 预处理字符串，可以将原本需要分奇偶讨论转变为一种情况。
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            # equals to i' = C - (i-C)
            P[i] = min(R - i, P[2 * C - i]) if R > i else 0

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


if __name__ == '__main__':
    s = Solution2()
    print(s.longestPalindrome('babcbabcbaccba'))
