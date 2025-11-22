# temp_conversion_tool.py


# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# Main program
if __name__ == "__main__":
   temperature_input = input("Enter the temperature: ")
   unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


# Validate temperature input
if temperature_input.replace('.', '', 1).replace('-', '', 1).isdigit() is False:
   raise ValueError("Invalid temperature. Please enter a numeric value.")
   temp = float(temperature_input)


if unit == "C":
    result = convert_to_fahrenheit('temp')
    print(f"{'temp'}°C is equal to {result:.2f}°F")


elif unit == "F":
    result = convert_to_celsius('temp')
    print(f"{'temp'}°F is equal to {result:.2f}°C")


else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
