1class Solution:
2    def judgeSquareSum(self, c: int) -> bool:
3        low = 0
4        high = c 
5        ans = 0
6        while low <= high:
7            mid = low + (high-low)//2
8            if mid * mid <= c:
9                ans = mid 
10                low = mid + 1 
11            else:
12                high = mid - 1 
13        
14        i = 0 
15        j = ans 
16        while i <= j:
17            tmp = i*i + j*j 
18            if tmp > c:
19                j -= 1 
20            elif tmp < c:
21                i += 1
22            else:
23                return True 
24        return False 