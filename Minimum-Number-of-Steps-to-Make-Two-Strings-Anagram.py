1class Solution:
2    def minSteps(self, s: str, t: str) -> int:
3        ct = Counter(t)
4        cs = Counter(s)
5        union = cs | ct
6        intersection = union & cs
7        return sum(union.values()) - sum(intersection.values()) 