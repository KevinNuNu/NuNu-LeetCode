from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        new_time = [t % 60 for t in time]
        c = Counter(new_time)
        res = 0
        for k, v in c.items():
            if k == 0 or k == 30:
                res += v * (v - 1) / 2
            else:
                tag = 60 - k
                if c.get(tag, None):
                    res += c[k] * c[tag] / 2
        return int(res)