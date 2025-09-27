class Solution:
    def fib(self, n: int) -> int:

        a=0

        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            a = self.fib(n-1) + self.fib(n-2)
        
        return a

        