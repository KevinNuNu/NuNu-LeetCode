class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return -1

        if n == 1:
            return 0

        idx1, idx2 = 0, n - 1

        while idx1 <= idx2:
            idx_mid = (idx1 + idx2) // 2
            if idx_mid == 0 and nums[idx_mid] > nums[idx_mid + 1]:
                return 0

            if idx_mid == n - 1 and nums[idx_mid] > nums[idx_mid - 1]:
                return n - 1

            if nums[idx_mid] > nums[idx_mid - 1] and nums[idx_mid] > nums[idx_mid + 1]:
                return idx_mid

            if nums[idx_mid] < nums[idx_mid + 1]:
                idx1 = idx_mid + 1
                continue

            if nums[idx_mid] < nums[idx_mid - 1]:
                idx2 = idx_mid - 1
                continue
