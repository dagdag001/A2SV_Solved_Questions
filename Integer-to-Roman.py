1class Solution:
2    def intToRoman(self, num: int) -> str:
3        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
4        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
5        hrns = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
6        ths  = ["","M","MM","MMM"]
7        
8        return (
9            ths[num // 1000] +
10            hrns[(num % 1000) // 100] +
11            tens[(num % 100) // 10] +
12            ones[num % 10]
13        )
14