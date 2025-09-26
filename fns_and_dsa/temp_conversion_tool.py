FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
temperature_input= input("Enter the temperature to convert: ")
temperature = float(temperature_input)
user_input2 = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
if user_input2 == "C":
    converted = convert_to_fahrenheit(float(temperature_input))
    print(f"{temperature_input}°C is {converted}°F.")
elif user_input2 == "F":
    converted = convert_to_celsius(float(temperature_input))
    print(f"{temperature_input}°F is {converted}°C.")
else:
    print("Invalid temperature. Please enter a numeric value.")