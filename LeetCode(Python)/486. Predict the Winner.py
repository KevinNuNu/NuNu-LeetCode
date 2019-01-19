class Solution:
    def PredictTheWinner4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [nums[i] for i in range(n)]

        for l in range(2, n+1):
            for i in range(n-l+1):
                dp[i] = max(nums[i] - dp[i+1], nums[i+l-1] - dp[i])
        return dp[0] >= 0

    def PredictTheWinner3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[-float('inf') for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        ifcal = [['no' for j in range(n)] for i in range(n)]

        def score(numbers, l, r):
            if l == r:
                return numbers[l]
            if ifcal[l][r] == 'no':
                ifcal[l][r] = max(numbers[l] - score(numbers, l + 1, r),
                                  numbers[r] - score(numbers, l, r - 1))
            return ifcal[l][r]

        return score(nums, 0, n-1) >= 0

    def PredictTheWinner1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def score(numbers, l, r):
            if l == r:
                return numbers[l]
            return max(numbers[l] - score(numbers, l+1, r), numbers[r] - score(numbers, l, r-1))

        return score(nums, 0, n-1) >= 0


if __name__ == '__main__':
    s = Solution()
    print(s.PredictTheWinner4([1,5,233,7]))