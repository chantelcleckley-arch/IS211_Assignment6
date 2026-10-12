
# IS211 - Assignment 6
# Week 6: Testing and Refactoring
# Part I - Celsius Conversion Tests

import unittest


from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import convert, ConversionNotPossible

class TestCelsiusConversions(unittest.TestCase):

    def test_celsius_to_kelvin(self):
        test_cases = [
            (0, 273.15),
            (100, 373.15),
            (-40, 233.15),
            (300, 573.15),
            (25, 298.15)
        ]

        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print(f"Testing {celsius} C to Kelvin")
                result = convertCelsiusToKelvin(celsius)
                self.assertAlmostEqual(result, expected)

    def test_celsius_to_fahrenheit(self):
        test_cases = [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (25, 77)
        ]

        for celsius, expected in test_cases:
            with self.subTest(celsius=celsius):
                print(f"Testing {celsius} C to Fahrenheit")
                result = convertCelsiusToFahrenheit(celsius)
                self.assertAlmostEqual(result, expected)


# Part III - Fahrenheit and Kelvin Tests

class TestFahrenheitKelvinConversions(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        cases = [
            (32, 0), (212, 100), (-40, -40),
            (77, 25), (98.6, 37)
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                print(f"Testing {value} F to Celsius")
                self.assertAlmostEqual(
                    convertFahrenheitToCelsius(value), expected
                )

    def test_fahrenheit_to_kelvin(self):
        cases = [
            (32, 273.15), (212, 373.15),
            (-40, 233.15), (77, 298.15),
            (98.6, 310.15)
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                print(f"Testing {value} F to Kelvin")
                self.assertAlmostEqual(
                    convertFahrenheitToKelvin(value), expected
                )

    def test_kelvin_to_celsius(self):
        cases = [
            (273.15, 0), (373.15, 100),
            (233.15, -40), (298.15, 25),
            (310.15, 37)
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                print(f"Testing {value} K to Celsius")
                self.assertAlmostEqual(
                    convertKelvinToCelsius(value), expected
                )

    def test_kelvin_to_fahrenheit(self):
        cases = [
            (273.15, 32), (373.15, 212),
            (233.15, -40), (298.15, 77),
            (310.15, 98.6)
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                print(f"Testing {value} K to Fahrenheit")
                self.assertAlmostEqual(
                    convertKelvinToFahrenheit(value), expected
                )



# Part IV - Refactored Conversion Tests

class TestRefactoredConversions(unittest.TestCase):

    def test_temperature_conversions(self):
        cases = [
            ("Celsius", "Fahrenheit", 100, 212),
            ("Celsius", "Kelvin", 0, 273.15),
            ("Fahrenheit", "Celsius", 32, 0),
            ("Fahrenheit", "Kelvin", 212, 373.15),
            ("Kelvin", "Celsius", 273.15, 0),
            ("Kelvin", "Fahrenheit", 273.15, 32)
        ]
        for from_unit, to_unit, value, expected in cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print(f"Testing {from_unit} to {to_unit}")
                self.assertAlmostEqual(
                    convert(from_unit, to_unit, value), expected
                )

    def test_distance_conversions(self):
        cases = [
            ("Miles", "Yards", 1, 1760),
            ("Miles", "Meters", 1, 1609.344),
            ("Yards", "Miles", 1760, 1),
            ("Yards", "Meters", 1, 0.9144),
            ("Meters", "Miles", 1609.344, 1),
            ("Meters", "Yards", 0.9144, 1)
        ]
        for from_unit, to_unit, value, expected in cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print(f"Testing {from_unit} to {to_unit}")
                self.assertAlmostEqual(
                    convert(from_unit, to_unit, value), expected
                )

    def test_same_unit(self):
        units = [
            "Celsius", "Fahrenheit", "Kelvin",
            "Miles", "Yards", "Meters"
        ]
        for unit in units:
            with self.subTest(unit=unit):
                print(f"Testing {unit} to itself")
                self.assertEqual(convert(unit, unit, 25), 25.0)

    def test_incompatible_units(self):
        cases = [
            ("Celsius", "Meters"),
            ("Miles", "Fahrenheit"),
            ("Kelvin", "Yards"),
            ("Meters", "Celsius")
        ]
        for from_unit, to_unit in cases:
            with self.subTest(from_unit=from_unit, to_unit=to_unit):
                print(f"Testing invalid conversion: {from_unit} to {to_unit}")
                with self.assertRaises(ConversionNotPossible):
                    convert(from_unit, to_unit, 25)



if __name__ == "__main__":
    unittest.main(verbosity=2)

