class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sortedcandidates = sorted(candidates)

        def iteration(c, cur, tag):
            if tag == 0:
                self.result.append(cur[:])
                return
            for idx, item in enumerate(c):
                if item > tag:
                    return
                # 这步是去重的关键
                # 利用[1,2...,n]的解一定是[1,1,1,2...,n]的解的子集特点
                # 判断c[idx] == c[idx-1]是否和前者相同，相同则跳过
                if idx != 0 and c[idx] == c[idx-1]:
                    continue
                cur.append(item)
                iteration(c[idx+1:], cur, tag-item)
                cur.pop(-1)
        iteration(sortedcandidates, [], target)
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
