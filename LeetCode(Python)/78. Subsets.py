class Solution(object):
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 位运算解法
        result = []
        subsets_size = 2 ** len(nums)
        n = 0
        while n < subsets_size:
            subset = []
            # 判断各位上是否是1
            i = 0
            bits = n
            while bits > 0:
                # bits & 1 == 1 代表bits末尾为1
                if bits & 1 == 1:
                    subset.append(nums[i])
                i += 1
                bits = bits >> 1
            n += 1
            result.append(subset)

        return result

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 迭代解法
        results = [[]]
        for num in nums:
            results += [result + [num] for result in results]
        return results

    def __init__(self):
        self.result = []

    def subsets3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 递归解法
        from copy import deepcopy

        def dfs(subset, cur_nums):
            self.result.append(deepcopy(subset))
            for idx, item in enumerate(cur_nums):
                subset.append(item)
                dfs(subset, cur_nums[idx+1:])
                subset.pop()
            return

        dfs([], nums)
        return self.result

