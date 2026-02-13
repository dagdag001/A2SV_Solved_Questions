1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        list_p = list(pattern)
4        list_s = s.split()
5        if len(list_s ) != len(list_p):
6            return False
7        res = list(zip(list_s, list_p))
8        h = {}
9        for i ,j in res:
10            if i not in h:
11                h[i] = [j]
12            else:
13                h[i].append(j)
14        for p, s  in h.items():
15            if len(set(s)) != 1:
16                return False
17        used = set()
18        for lst in h.values():
19            word = lst[0]
20            if word in used:
21                return False
22            used.add(word)
23        return True
24