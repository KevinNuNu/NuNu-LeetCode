class Solution(object):
    def __init__(self):
        self.result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []

        def dfs(left_element, cur, target):
            if target == 0:
                res = cur[:]
                self.result.append(res)
                return
            for idx, ele in enumerate(left_element):
                cur.append(ele)
                dfs(left_element[idx+1:], cur, target-1)
                cur.remove(ele)
            return

        all_ele = [i + 1 for i in range(n)]
        dfs(all_ele, [], k)

        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.combine(5, 3))
