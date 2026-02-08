1class Solution:
2    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
3        covered = set()
4
5        for start, end in ranges:
6            for i in range(start, end + 1):
7                covered.add(i)
8
9        for i in range(left, right + 1):
10            if i not in covered:
11                return False
12
13        return True