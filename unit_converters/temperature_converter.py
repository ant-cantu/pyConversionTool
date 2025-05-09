# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)

# Testing Purpose Only
if __name__ == "__main__":
    print("temperature_converter.py is being ran directly as the main program.")
    print("*** Example Usage ***")
    temp = 20 # Set initial temp to 20 celsius
    print(f"Converting {temp} celsius to fahrenheit: {celsius_to_fahrenheit(temp)}")
    temp = celsius_to_fahrenheit(temp) # Update new temp with conversion
    print(f"Converting {temp} fahrenheit to celsius: {fahrenheit_to_celsius(temp)}")
    # temp = fahrenheit_to_celsius(temp) # Update new temp with conversion
    print("*** End of Example Usage ***")