# length_converter.py

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet * 0.3048

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles * 1.60934

# Testing Purpose Only
if __name__ == "__main__":
    print("length_converter.py is being run directly as the main program.")
    print("*** Example Usage ***")
    # Testing unit conversion
    _units = meters_to_feet(10) # Convert 10 meters to feet 
    print(f"Converting 10 meters to feet: {_units} feet")
    print(f"Converting {_units} feet to meters: {feet_to_meters(_units)} meters")

    # Testing distance conversion
    _distance = kilometers_to_miles(10) # Convert 10 kilometers to miles
    print(f"Converting 10 kilometers to miles: {_distance} miles")
    print(f"Converting {_distance} miles to kilometers: {miles_to_kilometers(_distance)} kilometers")
    print("*** End of Example Usage ***")
