class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        covered = set()

        for start, end in ranges:
            for i in range(start, end + 1):
                covered.add(i)

        for i in range(left, right + 1):
            if i not in covered:
                return False

        return True