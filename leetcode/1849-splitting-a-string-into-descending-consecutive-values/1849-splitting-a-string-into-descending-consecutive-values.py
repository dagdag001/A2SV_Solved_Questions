class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev, count):
            if index == len(s):
                return count >= 2

            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])

                if num == prev - 1:
                    if dfs(i + 1, num, count + 1):
                        return True

                if num >= prev:
                    break

            return False

        first = 0
        for i in range(len(s) - 1):
            first = first * 10 + int(s[i])
            if dfs(i + 1, first, 1):
                return True

        return False