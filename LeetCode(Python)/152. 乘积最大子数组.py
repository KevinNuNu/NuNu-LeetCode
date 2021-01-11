class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        fmax = [0 for _ in range(n)]
        fmin = [0 for _ in range(n)]
        fmax[0], fmin[0] = nums[0], nums[0]
        for i in range(1, n):
            fmax[i] = max(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
            fmin[i] = min(fmax[i-1] * nums[i], fmin[i-1] * nums[i], nums[i])
        return max(fmax)