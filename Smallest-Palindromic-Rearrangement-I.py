class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        middle = ""
        half = []
        for ch in sorted(c.keys()):
            if c[ch] % 2 != 0:
                middle+=ch
            half.append(ch *( c[ch] // 2))
        half_str = "".join(half) 
        return half_str + middle + half_str[::-1]
