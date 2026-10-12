
# IS211 - Assignment 6
# Week 6: Testing and Refactoring
# Part II - Celsius Conversion Functions

def convertCelsiusToKelvin(celsius):
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32



# Part III - Fahrenheit and Kelvin Conversions

def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convertFahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15


def convertKelvinToFahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

