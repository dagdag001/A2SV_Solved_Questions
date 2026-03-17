class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x, n):
            if n == 0:
                return 1
            y = cal(x, n // 2)
            return y * y if n % 2 == 0 else x * y * y
        
        return cal(x, n) if n >= 0 else 1 / cal(x, -n)
