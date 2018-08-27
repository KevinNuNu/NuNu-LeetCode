class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        num_set = set(nums)
        for num in num_set:
            # 看似for里嵌套while,时间复杂度为O(n^2)
            # 但由于仅从"num-1 not in num_set"开始进行while
            # 所以实则所有元素仅遍历一遍，时间复杂度为O(n)
            if num - 1 not in num_set:
                curr_len = 1
                while num + 1 in num_set:
                    curr_len += 1
                    num += 1
                longest = max(longest, curr_len)

        return longest


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
