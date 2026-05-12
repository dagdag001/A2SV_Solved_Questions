class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def valid(s):
            return not (len(s) > 1 and s[0] == '0')

        def add_strings(a, b):
            carry = 0
            res = []
            i, j = len(a) - 1, len(b) - 1

            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0
                total = x + y + carry
                res.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(res[::-1])

        def dfs(i, a, b, count):
            if i == n:
                return count >= 3

            c = add_strings(a, b)
            if not num.startswith(c, i):
                return False

            return dfs(i + len(c), b, c, count + 1)

        for i in range(1, n):
            for j in range(i  + 1, n):
                a = num[:i]
                b = num[i:j]

                if not valid(a) or not valid(b):
                    continue

                if dfs(j, a, b, 2):
                    return True

        return False