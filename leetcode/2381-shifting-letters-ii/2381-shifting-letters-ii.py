class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0]  * (len(s) + 1)
        for l, r, k in shifts:
            prefix_diff[l] += -1 if k == 1 else 1
            prefix_diff[r + 1] +=1 if k == 1 else -1
        res = [ord(c) - ord("a") for c in s]
        diff = 0
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i-1] = (diff + res[i-1]) % 26
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)




