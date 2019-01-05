import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        new_nums = self.nums
        res = 0
        count = 0
        for index, item in enumerate(new_nums):
            if item == target:
                count += 1
                k = random.randint(1, count)
                if k == 1:
                    res = index

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
