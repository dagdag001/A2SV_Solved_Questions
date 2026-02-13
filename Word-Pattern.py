class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_p = list(pattern)
        list_s = s.split()
        if len(list_s) != len(list_p):
            return False
        res = list(zip(list_s, list_p))
        h = {}
        for i, j in res:
            if i not in h:
                h[i] = [j]
            else:
                h[i].append(j)
        for p, s in h.items():
            if len(set(s)) != 1:
                return False
        used = set()
        for lst in h.values():
            word = lst[0]
            if word in used:
                return False
            used.add(word)
        return True