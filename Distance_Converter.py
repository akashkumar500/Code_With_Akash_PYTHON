from_unit = input("Enter the unit of distance to convert from (km, miles, m, feet, cm, inch, nautical mile, millimeter, yard): ").lower()
dist = float(input("Enter the distance: "))
to_unit = input("Enter the unit of distance to convert to (km, miles, m, feet, cm, inch, nautical mile, millimeter, yard): ").lower()

units = {
    "km": {"miles": 0.621371, "m": 1000, "feet": 3280.84, "cm": 100000, "inch": 39370.1, "nautical mile": 0.539957,
           "millimeter": 1000000, "yard": 1093.61},
           
    "miles": {"km": 1.60934, "m": 1609.34, "feet": 5280, "cm": 160934, "inch": 63360, "nautical mile": 0.868976,
              "millimeter": 1609344, "yard": 1760},
              
    "m": {"km": 0.001, "miles": 0.000621371, "feet": 3.28084, "cm": 100, "inch": 39.3701, "nautical mile": 0.000539957,
           "millimeter": 1000, "yard": 1.09361},
           
    "feet": {"km": 0.0003048, "miles": 0.000189394, "m": 0.3048, "cm": 30.48, "inch": 12, "nautical mile": 0.000164579,
             "millimeter": 304.8, "yard": 0.333333},
             
    "cm": {"km": 0.00001, "miles": 0.00000621371, "m": 0.01, "feet": 0.0328084, "inch": 0.393701, "nautical mile": 0.00000539957,
            "millimeter": 10, "yard": 0.0109361},
            
    "inch": {"km": 0.0000254, "miles": 0.0000157828, "m": 0.0254, "feet": 0.0833333, "cm": 2.54, "nautical mile": 0.0000137149,
             "millimeter": 25.4, "yard": 0.0277778},
             
    "nautical mile": {"km": 1.852, "miles": 1.15078, "m": 1852, "feet": 6076.12, "cm": 185200, "inch": 72913.4,
                    "millimeter": 1852000, "yard": 2025.37},
                      
    "millimeter": {"km": 0.000001, "miles": 0.000000621371, "m": 0.001, "feet": 0.00328084, "cm": 0.1, "inch": 0.0393701,
                   "nautical mile": 0.000000539957, "yard": 0.00109361},
                   
    "yard": {"km": 0.0009144, "miles": 0.000568182, "m": 0.9144, "feet": 3, "cm": 91.44, "inch": 36, "nautical mile": 0.000493737,
             "millimeter": 914.4}
}

if from_unit in units and to_unit in units[from_unit]:
    converted_distance = dist * units[from_unit][to_unit]
    print(f"{dist} {from_unit} is equal to {converted_distance} {to_unit}")
else:
    print("Invalid units")
