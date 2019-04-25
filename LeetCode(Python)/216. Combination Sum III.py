class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i + 1 for i in range(9)]

        def dfs(curr, left_nums, left_n, left_k):
            if left_k == 0 and left_n == 0:
                self.result.append(curr[:])
                return
            elif left_k == 0 and left_n != 0:
                return
            else:
                for i in range(len(left_nums)):
                    curr.append(left_nums[i])
                    dfs(curr, left_nums[i+1:], left_n-left_nums[i], left_k-1)
                    curr.pop()
                return

        dfs([], nums, n, k)

        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 9))