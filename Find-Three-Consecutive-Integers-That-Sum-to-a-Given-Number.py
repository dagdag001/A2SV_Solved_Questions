1class Solution:
2    def sumOfThree(self, num: int) -> List[int]:
3        # x + x+1 + x+ 2 => 3x + 3 = num 
4        # x = (num - 3) / 3 
5        x = (num - 3) / 3
6        if x.is_integer():
7            x = int(x)
8            return [x, x+1, x+2]
9        else:
10            return []
11        