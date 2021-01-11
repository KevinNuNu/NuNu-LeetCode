import bisect


class Solution:
    """
    该解题方法称为patient sorting(参考当空接龙纸牌游戏)
    因为维护的dp数组为递增序列，用到了二分查找，时间复杂度可以降低到O(nlogn)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示长度为i+1的最长递增子序列的末尾数值
        n = len(nums)
        dp = [nums[0]]
        for i in range(1, n):
            idx = bisect.bisect_left(dp, nums[i])
            if idx == len(dp): 
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
        return len(dp)