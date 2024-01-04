class Solution:
    def convertTemperature(self, celsius):
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round(celsius * 1.80 + 32.00, 5)
        return [kelvin, fahrenheit]
