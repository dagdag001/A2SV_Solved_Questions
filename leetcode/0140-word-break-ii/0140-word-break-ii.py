class Solution:
    def wordBreak(self, s: str, wordDict):
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            res = []
            word = ""

            for end in range(start, len(s)):
                word += s[end]

                if word in word_set:
                    for suffix in dfs(end + 1):
                        if suffix == "":
                            res.append(word)
                        else:
                            res.append(word + " " + suffix)

            memo[start] = res
            return res

        return dfs(0)