class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        res = [0] * (n + 1)
        res[0] = 0
        res[1] = 1
        res[2] = 2
        res[3] = 3

        for i in range(4, n+1):
            max_res = 0
            for j in range(1, (i>>1)+1):
                product = res[j] * res[i-j]
                if max_res < product:
                    max_res = product
            res[i] = max_res
        
        return res[-1]