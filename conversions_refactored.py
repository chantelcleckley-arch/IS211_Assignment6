
# IS211 - Assignment 6
# Part IV - Refactoring

class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):

    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

    distance_factors = {
        "Miles": 1609.344,
        "Yards": 0.9144,
        "Meters": 1.0
    }

    # Check if the units are identical
    if fromUnit == toUnit:
        if fromUnit in temperature_units or fromUnit in distance_factors:
            return float(value)
        raise ConversionNotPossible("Unknown unit")

    # Temperature conversions
    if fromUnit in temperature_units and toUnit in temperature_units:

        # Convert the starting temperature to Celsius
        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        else:
            celsius = value - 273.15

        # Convert Celsius to the requested unit
        if toUnit == "Celsius":
            return float(celsius)
        elif toUnit == "Fahrenheit":
            return float(celsius * 9 / 5 + 32)
        else:
            return float(celsius + 273.15)

    # Distance conversions
    if fromUnit in distance_factors and toUnit in distance_factors:
        meters = value * distance_factors[fromUnit]
        return float(meters / distance_factors[toUnit])

    # Incompatible or unknown units
    raise ConversionNotPossible(
        f"Cannot convert {fromUnit} to {toUnit}"
    )

