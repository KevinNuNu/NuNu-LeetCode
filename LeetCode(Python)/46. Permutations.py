class Solution(object):
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # python内建函数方法
        from itertools import permutations

        return [list(item) for item in permutations(nums)]

    def __init__(self):
        self.result = []

    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        def backtrack(cur, left_nums):
            if len(left_nums) == 1:
                temp = cur[:]
                temp.append(left_nums[0])
                self.result.append(temp)
                return
            for i in range(len(left_nums)):
                cur.append(left_nums[i])
                backtrack(cur, left_nums[:i] + left_nums[i+1:])
                cur.pop()
            return

        backtrack([], nums)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.permute2([1, 2, 3]))
