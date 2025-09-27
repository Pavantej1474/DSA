class Solution:
    def fib(self, n: int) -> int:

        a=0

        if n<2:
            return n
        else:
            a = self.fib(n-1) + self.fib(n-2)
        
        return a

        