1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        h = defaultdict(list)
4        for i in strs:
5            k = tuple(sorted(i))
6            h[k].append(i)
7        return list(h.values())
8