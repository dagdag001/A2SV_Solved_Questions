class Solution:
    def distributeCookies(self, cookies, k):
        n = len(cookies)
        children = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == n:
                self.ans = min(self.ans, max(children))
                return
            if max(children) >= self.ans:
                return

            seen = set() 

            for j in range(k):
                if children[j] in seen:
                    continue
                seen.add(children[j])

                children[j] += cookies[i]
                backtrack(i + 1)
                children[j] -= cookies[i]

                if children[j] == 0:
                    break

        backtrack(0)
        return self.ans