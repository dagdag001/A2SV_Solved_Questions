class Solution:
    def romanToInt(self, s: str) -> int:
       
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        special_case = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
            'CD': 400, 'CM': 900
        }
        
        integer = 0
        i= 0
        n = len(s)

        while i < n:
            if s[i:i+2:] in special_case:
                integer+= special_case[s[i:i+2:]]
                i+=2
            else:
                integer+= roman[s[i]]
                i+=1




        return integer
            
