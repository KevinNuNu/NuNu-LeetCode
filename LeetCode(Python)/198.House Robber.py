class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        n = len(nums)
        rob_money1 = 0
        rob_money2 = 0
        rob_money3 = 0

        for i in range(n):
            rob_money3 = max((rob_money1 if i > 1 else 0)+nums[i], (rob_money2 if i > 0 else 0))
            rob_money1 = rob_money2
            rob_money2 = rob_money3

        return rob_money3
