class Solution(object):
    def subsetsWithDup1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 迭代解法
        result = [[]]
        nums.sort()
        for num in nums:
            result = result + [item + [num] for item in result if (item + [num]) not in result]

        return result

    def __init__(self):
        self.result = []

    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 递归解法
        from copy import deepcopy

        def dfs(subset, cur_nums):
            self.result.append(deepcopy(subset))
            for idx, item in enumerate(cur_nums):
                if idx != 0 and item == cur_nums[idx-1]:
                    continue
                subset.append(item)
                dfs(subset, cur_nums[idx+1:])
                subset.pop()
            return

        nums.sort()
        dfs([], nums)

        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup2([4, 4, 4, 1, 4]))
