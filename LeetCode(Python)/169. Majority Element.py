class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = n // 2
        num_set = set(nums)
        for num in num_set:
            if nums.count(num) > target:
                return num
