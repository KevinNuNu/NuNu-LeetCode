class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        maxlength = 0
        char_dict = {}
        start_index = 0
        for index, char in enumerate(s):
            # 不存在就加入字典，并更新长度
            # 存在，且之前的字母处在substring中，需要更新start位置；不在substring中则无影响
            if char_dict.get(char, None) is not None and char_dict[char] >= start_index:
                start_index = char_dict[char] + 1
            sublength = index - start_index + 1
            char_dict[char] = index
            maxlength = max(maxlength, sublength)

        return maxlength


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

