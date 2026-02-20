1class Solution:
2    def minimumSwap(self, s1: str, s2: str) -> int:
3        xy = yx = 0
4        
5        for a, b in zip(s1, s2):
6            if a == 'x' and b == 'y':
7                xy += 1
8            elif a == 'y' and b == 'x':
9                yx += 1
10        
11        if (xy + yx) % 2 != 0:
12            return -1
13        
14        swaps = xy // 2 + yx // 2
15        if xy % 2 == 1:
16            swaps += 2
17        
18        return swaps