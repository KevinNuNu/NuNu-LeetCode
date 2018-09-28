class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        pre = x
        post = 0
        while pre > post:
            post = post * 10 + pre % 10
            pre = pre // 10

        return pre == post or pre == post // 10

