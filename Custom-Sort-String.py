class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {ch:odr for odr, ch in enumerate(order)}
        return "".join(sorted(s, key = lambda x: rank.get(x, len(order))))