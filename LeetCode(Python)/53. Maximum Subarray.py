class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            res = nums[0]
            curr = nums[0]
            for i in nums[1:]:
                if curr <= 0:
                    curr = 0
                curr += i
                res = max(res, curr)
            return res
        else:
            return None


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1]))
