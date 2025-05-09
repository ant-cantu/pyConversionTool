# main_converter.py

# Import custom modules
from unit_converters import length_converter as lc
from unit_converters import temperature_converter as tc

# Main Program
print("*** Simple Conversion Tool ***\n")
while True:
    try:
        print("1. Length Conversion")
        print("2. Temperature Conversion")
        print("3. Exit Application")
        selection = int(input("Select an option (1-3): ")) # Ensure input is numeric

        if selection == 1:
            while True:
                print("\n*** Length Conversion ***\n")
                print("1. Meters to feet")
                print("2. Feet to meters")
                print("3. Kilometers to miles")
                print("4. Miles to kilometers")
                print("5. Go back")
                sub_selection = int(input("Select an option (1-5): "))

                if sub_selection == 1:
                    unit = float(input("\nPlease enter the meters unit to convert: "))
                    print(f"Meters to feet conversion: {lc.meters_to_feet(unit)}\n")
                    break
                elif sub_selection == 2:
                    unit = float(input("\nPlease enter the feet units to convert: "))
                    print(f"Feet to meters conversion: {lc.feet_to_meters(unit)}\n")
                    break
                elif sub_selection == 3:
                    distance = float(input("\nPlease enter the kilometers to convert: "))
                    print(f"Kilometers to miles conversion: {lc.kilometers_to_miles(distance)}\n")
                    break
                elif sub_selection == 4:
                    distance = float(input("\nPlease enter the miles to convert: "))
                    print(f"Miles to kilometers conversion: {lc.miles_to_kilometers(distance)}\n")
                    break
                elif sub_selection == 5:
                    print("\n") # Line break
                    break
                else:
                    print("\nError: Please input a valid selection")
        elif selection == 2:
            while True:
                print("\n*** Temperature Conversion ***\n")
                print("1. Celsius to fahrenheit")
                print("2. Fahrenheit to celsius")
                print("3. Go back")
                sub_selection = int(input("Select an option (1-3): "))

                if sub_selection == 1:
                    temp = float(input("\nPlease enter temperature in celsius to convert: "))
                    print(f"Celsius to fahrenheit: {tc.celsius_to_fahrenheit(temp)}\n")
                    break
                elif sub_selection == 2:
                    temp = float(input("\nPlease enter temperature in fahrenheit to convert: "))
                    print(f"Fahrenheit to celsius: {tc.fahrenheit_to_celsius(temp)}\n")
                    break
                elif sub_selection == 3:
                    print("\n") # Line break
                    break
                else:
                    print("\nError: Please input a valid selection.")
        elif selection == 3:
            print("\nExiting Application")
            break
        else:
            print("\nError: Please input a valid selection\n")
    except ValueError:
        print("\nError: Please input a valid selection.\n")
