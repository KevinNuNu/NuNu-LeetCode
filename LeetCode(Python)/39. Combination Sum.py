class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sortedcandidates = sorted(set(candidates))

        def iteration(c, cur, tag, lastc):
            if tag == 0:
                self.result.append(cur[:])
                return
            for i in c:
                if i > tag:
                    return
                if i < lastc:
                    continue
                cur.append(i)
                iteration(c, cur, tag-i, i)
                cur.pop(-1)
        iteration(sortedcandidates, [], target, sortedcandidates[0])
        return self.result
