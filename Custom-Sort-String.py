1class Solution:
2    def customSortString(self, order: str, s: str) -> str:
3        rank = {ch:odr for odr, ch in enumerate(order)}
4        return "".join(sorted(s, key = lambda x: rank.get(x, len(order))))