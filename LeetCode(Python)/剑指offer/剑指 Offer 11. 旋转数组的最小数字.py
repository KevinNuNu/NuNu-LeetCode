from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return None
        
        i, j = 0, len(numbers)-1
        mid = 0
        while numbers[i] >= numbers[j]:

            if j - i == 1:
                mid = j
                break
            mid = (i + j) >> 1

            # 特殊情况，如果numbers[i] == numbers[mid] == numbers[j],则需要顺序查找
            # 例如【1，0，1，1，1】/【1，1，1，0，1】
            if (numbers[i] == numbers[mid]) and (numbers[mid] == numbers[j]):
                return self.minInOrder(numbers, i, j)

            if numbers[mid] >= numbers[i]:
                i = mid
            elif numbers[mid] <= numbers[j]:
                j = mid

        return numbers[mid]
    
    def minInOrder(self, num, i, j):
        res = num[i]
        for k in range(i, j+1):
            if num[k] < res:
                res = num[k]
        return res

s = Solution()
print(s.minArray([1,0,1,1,1]))
