from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        char_dict = {}
        for num in nums:
            if not char_dict.get(num, None):
                char_dict[num] = 1
            else:
                break
        return num

