class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for string in strs:
                if string[i] != c:
                    return shortest[:i]
        return shortest
