class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = []
        for c in s:
            if len(stack) == 0:
                if c in ['(', '[', '{']:
                    stack.append(c)
                    continue
                else:
                    return False

            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if (c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{'):
                    stack.pop(-1)
                else:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()[]{}'))
