class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        s = 0
        e = length - 1
        max_area = 0
        while e - s >= 1:
            area = (e - s) * min(height[s], height[e])
            max_area = max(max_area, area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return int(max_area)


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,3,2,5,25,24,5]))