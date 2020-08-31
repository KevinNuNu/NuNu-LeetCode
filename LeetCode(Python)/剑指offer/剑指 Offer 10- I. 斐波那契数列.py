# 迭代的方法
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        fib0, fib1 = 0, 1
        for _ in range(n-1):
            fib2 = fib0 + fib1
            fib0, fib1 = fib1, fib2

        return fib2 % 1000000007

# 递归的方法更耗时，n大了以后，递归栈复杂度增加
class Solution1:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1

        return (self.fib(n-1) + self.fib(n-2)) % 1000000007

s = Solution()
print(s.fib(100))

s1 = Solution1()
print(s1.fib(100))