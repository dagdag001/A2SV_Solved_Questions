class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for i in strs:
            k = tuple(sorted(i))
            h[k].append(i)
        return list(h.values())
