class Solution:
    def isHappy(self, n: int) -> bool:
        def divideNumber(num):
            digits = []
            while num > 0:
                digits.append(num%10)
                num //=10
            return digits
        while n >6:
            n = sum(x**2 for x in divideNumber(n))
        if n == 1:
            return True
        else: 
            return False