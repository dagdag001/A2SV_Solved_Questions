class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        res = []
        cc = Counter(changed)
        for i in sorted(cc):
            if i == 0:
                if cc[0] % 2 != 0:
                    return []
                res.extend([0] * (cc[0] // 2))
                continue
            if cc[i] > cc[i*2]:
                return []
            for _ in range(cc[i]):
                res.append(i)
                cc[i*2] -=1
        return res
