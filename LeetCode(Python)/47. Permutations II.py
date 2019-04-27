class Solution(object):
    def permuteUnique1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations

        all_res = [list(item) for item in permutations(nums)]
        res = []
        for item in all_res:
            if item not in res:
                res.append(item)

        return res

    def __init__(self):
        self.result = []

    def permuteUnique2(self, nums):
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
                if i != 0 and left_nums[i] == left_nums[i-1]:
                    continue
                cur.append(left_nums[i])
                backtrack(cur, left_nums[:i] + left_nums[i+1:])
                cur.pop()
            return

        nums.sort()
        backtrack([], nums)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique2([3, 3, 0, 3]))
