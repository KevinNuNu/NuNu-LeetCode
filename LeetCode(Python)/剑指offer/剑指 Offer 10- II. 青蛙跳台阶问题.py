class Solution:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2

        fib0, fib1 = 1, 2
        for _ in range(n-2):
            fib2 = fib0 + fib1
            fib0, fib1 = fib1, fib2

        return fib2 % 1000000007