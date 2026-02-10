1class Solution:
2    def romanToInt(self, s: str) -> int:
3       
4        roman = {
5            'I': 1, 'V': 5, 'X': 10, 'L': 50,
6            'C': 100, 'D': 500, 'M': 1000
7        }
8        
9        special_case = {
10            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
11            'CD': 400, 'CM': 900
12        }
13        
14        integer = 0
15        i= 0
16        n = len(s)
17
18        while i < n:
19            if s[i:i+2:] in special_case:
20                integer+= special_case[s[i:i+2:]]
21                i+=2
22            else:
23                integer+= roman[s[i]]
24                i+=1
25
26
27
28
29        return integer
30            
31