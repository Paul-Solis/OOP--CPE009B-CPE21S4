def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
#formula to celsius to farenheit
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
#formula to celsius to kelvin
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15
#formula to farenheit to celsius
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9
#formula to kelvin to celsius
    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15


    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")


    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")


    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")


main()