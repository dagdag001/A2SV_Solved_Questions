1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def divideNumber(num):
4            digits = []
5            while num > 0:
6                digits.append(num%10)
7                num //=10
8            return digits
9        while n >6:
10            n = sum(x**2 for x in divideNumber(n))
11        if n == 1:
12            return True
13        else: 
14            return False