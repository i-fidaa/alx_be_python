FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    converted_temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return converted_temperature

def convert_to_fahrenheit(celsius):
    converted_temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return converted_temperature

try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result}°F")
elif unit == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
else:
    print("Invalid unit.")
