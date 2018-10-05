# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) < 3:
#             return []
#
#         res = []
#         # 排序的时间复杂度O(nlogn)不影响整体O(n^2)的复杂度，所以可以先排序
#         nums.sort()
#         for index, num in enumerate(nums):
#             # 遇到num[i] = num[i+1]相等的跳过即可，否则会出现重复结果
#             if index >= 1 and nums[index-1] == num:
#                 continue
#
#             left, right = index+1, len(nums)-1
#             while left < right:
#                 left_v, right_v = nums[left], nums[right]
#                 total = num + left_v + right_v
#                 if total < 0:
#                     left += 1
#                 elif total > 0:
#                     right -= 1
#                 else:
#                     res.append([num, left_v, right_v])
#                     # 此处必须两边同时“向中间压缩”，且不能与之前相同才行
#                     while left < right and nums[left + 1] == left_v:
#                         left += 1
#                     while left < right and nums[right - 1] == right_v:
#                         right -= 1
#                     left += 1
#                     right -= 1
#         return res


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = dict()
        for i in range(len(nums)):
            # 统计num出现次数
            tmp[nums[i]] = tmp.get(nums[i], 0) + 1
        # 按照目标进行“二分”，相较上面那种方法，虽然时间复杂度都是O(n^2)，
        # 但前者是O(n^2/2)，后者“二分”后则是O(n^2/4)，更快
        # 此处用字典计数，也起到了“去重”的效果，后面的判断都是根据去重后的“key”来做的，
        # 所以仅需将“三数都相同”的特殊情况（此处为[0,0,0]，若要求和为3，则为[1,1,1]）进行单独考虑即可。
        left = sorted(filter(lambda x: x < 0, tmp))
        right = sorted(filter(lambda x: x >= 0, tmp))
        if 0 in tmp and tmp[0] > 2:
            res = [[0, 0, 0]]
        else:
            res = []
        for i in left:
            for j in right:
                mid = -i - j
                if mid in tmp:
                    if mid in (i, j) and tmp[mid] > 1:
                        res.append([i, mid, j])
                    elif i < mid < j:
                        res.append([i, mid, j])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
