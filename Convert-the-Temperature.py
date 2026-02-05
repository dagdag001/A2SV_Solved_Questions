1class Solution:
2    def convertTemperature(self, celsius: float) -> list[float]:
3        kelvin = celsius + 273.15
4        fahrenheit = celsius * 1.8 + 32
5        
6        return [kelvin, fahrenheit]
7