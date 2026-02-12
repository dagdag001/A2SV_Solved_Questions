class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ct = Counter(t)
        cs = Counter(s)
        union = cs | ct
        intersection = union & cs
        return sum(union.values()) - sum(intersection.values()) 