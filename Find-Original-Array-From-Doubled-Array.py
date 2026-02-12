1class Solution:
2    def findOriginalArray(self, changed: List[int]) -> List[int]:
3        if len(changed) % 2 != 0:
4            return []
5        res = []
6        cc = Counter(changed)
7        for i in sorted(cc):
8            if i == 0:
9                if cc[0] % 2 != 0:
10                    return []
11                res.extend([0] * (cc[0] // 2))
12                continue
13            if cc[i] > cc[i*2]:
14                return []
15            for _ in range(cc[i]):
16                res.append(i)
17                cc[i*2] -=1
18        return res
19
20        