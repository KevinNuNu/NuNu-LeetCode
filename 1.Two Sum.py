class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index_dict = {}
        for index, x in enumerate(nums):
            if index_dict.get(x, None) is None:
                index_dict[x] = [index]
            else:
                index_dict[x].append(index)

        for x in nums:
            if index_dict.get(target-x, None) is None:
                continue
            elif index_dict[x] == index_dict[target-x]:
                if len(index_dict[x]) == 1:
                    continue
                else:
                    return [index_dict[x][0], index_dict[x][1]]
            else:
                return [index_dict[x][0], index_dict[target-x][0]]


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
