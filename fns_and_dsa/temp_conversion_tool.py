FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Pleaase enter a numeric value.")

def convert_to_celsius(fahrenheit):
    converted_temperature = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted_temperature

def convert_to_fahrenheit(celsius):
    converted_temperature = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return converted_temperature

unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
if unit == "C" :
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F") 
elif unit == "F" :
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
else :
    print("Invalid unit.")