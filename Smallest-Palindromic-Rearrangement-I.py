1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        c = Counter(s)
4        middle = ""
5        half = []
6        for ch in sorted(c.keys()):
7            if c[ch] % 2 != 0:
8                middle+=ch
9            half.append(ch *( c[ch] // 2))
10        half_str = "".join(half) 
11        return half_str + middle + half_str[::-1]
12            
13
14            
15